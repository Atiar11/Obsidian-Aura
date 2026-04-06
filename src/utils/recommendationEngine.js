import { PERFUME_DATABASE } from '../data/perfumeDatabase';

export const getRecommendations = (preferences) => {
  if (!preferences) return { budget: [], designer: [], niche: [] };

  const userGender = preferences.gender || 'unisex';
  const userVibes = Array.isArray(preferences.vibe) ? preferences.vibe : [];
  const userOccasions = Array.isArray(preferences.occasion) ? preferences.occasion : [];
  const userPowers = Array.isArray(preferences.power) ? preferences.power : [];
  const userContexts = Array.isArray(preferences.context) ? preferences.context : [];
  const userPsych = Array.isArray(preferences.psychology) ? preferences.psychology : [];

  const scored = [];

  for (const perfume of PERFUME_DATABASE) {
    // Null-safety: ensure all fields exist as arrays
    const pVibes = Array.isArray(perfume.vibe) ? perfume.vibe : [];
    const pOccasions = Array.isArray(perfume.occasion) ? perfume.occasion : [];
    const pPowers = Array.isArray(perfume.power) ? perfume.power : [];
    const pContexts = Array.isArray(perfume.context) ? perfume.context : [];
    const pPsych = Array.isArray(perfume.psychology) ? perfume.psychology : [];
    const pGender = perfume.gender || 'unisex';

    // 1. Hard Gender Filter (Crucial)
    if (userGender !== 'unisex') {
      if (pGender !== userGender && pGender !== 'unisex') continue;
    }

    // 2. Hard Seasonality Filter (Crucial Accuracy)
    // If the user selects Hot or Cold Weather, we must never show the polar opposite.
    if (userContexts.includes('Hot Weather') && pContexts.includes('Cold Weather') && !pContexts.includes('Hot Weather') && !pContexts.includes('All Weather')) {
      continue;
    }
    if (userContexts.includes('Cold Weather') && pContexts.includes('Hot Weather') && !pContexts.includes('Cold Weather') && !pContexts.includes('All Weather')) {
      continue;
    }

    // 3. Weighted Scoring System (The "Oracle's" Logic)
    let score = 0;
    let matchCount = 0; // Track how many categories actually match

    // Vibe match (High priority)
    const vibeMatches = userVibes.filter(v => pVibes.includes(v)).length;
    if (vibeMatches > 0) {
      score += vibeMatches * 10;
      matchCount++;
    }

    // Occasions (Medium priority)
    const occasionMatches = userOccasions.filter(o => pOccasions.includes(o)).length;
    if (occasionMatches > 0) {
      score += occasionMatches * 8;
      matchCount++;
    }

    // Powers (Supportive priority)
    const powerMatches = userPowers.filter(p => pPowers.includes(p)).length;
    if (powerMatches > 0) {
      score += powerMatches * 5;
      matchCount++;
    }

    // Contexts (Supportive priority & seasonality bonus)
    const contextMatches = userContexts.filter(c => {
      if (pContexts.includes(c)) return true;
      if (pContexts.includes('All Weather') && (c === 'Hot Weather' || c === 'Cold Weather')) return true;
      return false;
    }).length;
    if (contextMatches > 0) {
      score += contextMatches * 5;
      matchCount++;
    }

    // Psychology (High priority - it's a driver)
    const psychMatches = userPsych.filter(ps => pPsych.includes(ps)).length;
    if (psychMatches > 0) {
      score += psychMatches * 15;
      matchCount++;
    }

    // Requirement: Must match at least 2 categories (to avoid generic spam)
    // Unless the user only selected 1 or 2 options total (rare).
    if (matchCount < 2) continue;

    // Add tiny random tiebreaker so identical scores vary across sessions
    const tiebreaker = Math.random() * 0.5;
    scored.push({ ...perfume, matchScore: score + tiebreaker, matchCount });
  }

  // Sort highest score first
  scored.sort((a, b) => b.matchScore - a.matchScore);

  return {
    niche: scored.filter(p => p.price_category === 'niche').slice(0, 15),
    designer: scored.filter(p => p.price_category === 'designer').slice(0, 15),
    budget: scored.filter(p => p.price_category === 'budget').slice(0, 15),
  };
};
