import gis from 'g-i-s';
import fs from 'fs';
import https from 'https';
import http from 'http';
import path from 'path';

const perfumes = [
  { term: "Dior Sauvage Elixir bottle isolated", file: "sauvage_elixir.webp" },
  { term: "Bleu de Chanel Parfum bottle isolated", file: "bleu_chanel.webp" },
  { term: "Lattafa Asad perfume bottle isolated", file: "lattafa_asad.webp" },
  { term: "YSL Libre Intense bottle isolated", file: "ysl_libre.webp" },
  { term: "Baccarat Rouge 540 Extrait bottle isolated", file: "br540.webp" },
  { term: "Carolina Herrera Good Girl perfume bottle isolated", file: "good_girl.webp" },
  { term: "Nautica Voyage bottle isolated", file: "nautica.webp" },
  { term: "Tom Ford Black Orchid bottle isolated", file: "black_orchid.webp" },
  { term: "Ariana Grande Cloud perfume bottle isolated", file: "cloud.webp" },
  { term: "Creed Aventus bottle isolated", file: "aventus.webp" }
];

const dest = path.join(process.cwd(), 'public', 'images');
if (!fs.existsSync(dest)) {
  fs.mkdirSync(dest, { recursive: true });
}

function downloadImage(url, filepath) {
  return new Promise((resolve, reject) => {
    const prot = url.startsWith('https') ? https : http;
    prot.get(url, (res) => {
      if (res.statusCode === 200) {
        const file = fs.createWriteStream(filepath);
        res.pipe(file);
        file.on('finish', () => {
          file.close();
          resolve(true);
        });
      } else {
        reject(new Error(`Failed with status code ${res.statusCode}`));
      }
    }).on('error', (err) => {
      reject(err);
    });
  });
}

async function processPerfumes() {
  for (const p of perfumes) {
    console.log(`Searching for: ${p.term}`);
    await new Promise((resolve) => {
      gis(p.term, async (error, results) => {
        if (error) {
          console.error(`Error searching ${p.term}:`, error);
          resolve();
          return;
        }

        if (results && results.length > 0) {
          let downloaded = false;
          // Try up to 3 links in case some 403 or fail
          for (let i = 0; i < Math.min(3, results.length); i++) {
            const imgUrl = results[i].url;
            console.log(`Trying ${imgUrl}`);
            try {
              await downloadImage(imgUrl, path.join(dest, p.file));
              console.log(`Successfully downloaded ${p.file}`);
              downloaded = true;
              break;
            } catch (err) {
              console.log(`Failed to download ${imgUrl}: ${err.message}`);
            }
          }
          if (!downloaded) console.log(`Failed all attempts for ${p.file}`);
        } else {
          console.log(`No results for ${p.term}`);
        }
        resolve(); // proceed to next
      });
    });
  }
}

processPerfumes().then(() => console.log('Done downloading images.'));
