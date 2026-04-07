import React, { useState, useMemo, useEffect } from 'react';
import { useSearchParams } from 'react-router-dom';
import { PERFUME_DATABASE } from '../../data/perfumeDatabase';
import '../Quiz/Results.css';
import './Encyclopedia.css';

const ITEMS_PER_PAGE = 20;

// Extracted outside component to avoid re-mount on every keystroke
const PerfumeCard = ({ perfume }) => {
  const notes = Array.isArray(perfume.notes) ? perfume.notes : [];
  const vibe = Array.isArray(perfume.vibe) ? perfume.vibe : [];

  return (
    <div className="perfume-card glass-panel ency-card">
      <div className="decoration corner-tl"></div>
      <div className="decoration corner-br"></div>
      <div className="perfume-img-container">
        <img
          src={perfume.aesthetic_image || 'https://images.unsplash.com/photo-1594035910387-fea47794261f?q=80&w=400&h=500&fit=crop'}
          alt={perfume.name}
          className="perfume-img"
          onError={(e) => {
            e.target.onerror = null;
            e.target.src = 'https://images.unsplash.com/photo-1594035910387-fea47794261f?q=80&w=400&h=500&fit=crop';
          }}
        />
      </div>
      <div className="perfume-details">
        <h3 className="perfume-name serif-text">{perfume.name}</h3>
        <p className="perfume-brand">{perfume.brand}</p>
        <p className="perfume-desc">{perfume.description}</p>
        <div className="perfume-stats">
          <div className="stat">
            <span className="stat-label">Gender:</span>
            <span className="stat-value" style={{ textTransform: 'capitalize' }}>{perfume.gender}</span>
          </div>
          <div className="stat">
            <span className="stat-label">Price:</span>
            <span className="stat-value">{perfume.price_range}</span>
          </div>
          {notes.length > 0 && (
            <div className="stat">
              <span className="stat-label">Notes:</span>
              <span className="stat-value">{notes.slice(0,4).join(', ')}</span>
            </div>
          )}
          {vibe.length > 0 && (
            <div className="stat">
              <span className="stat-label">Vibe:</span>
              <span className="stat-value">{vibe.join(', ')}</span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

function Encyclopedia() {
  const [searchParams, setSearchParams] = useSearchParams();
  const queryParam = searchParams.get('q') || '';

  const [searchTerm, setSearchTerm] = useState(queryParam);
  const [genderFilter, setGenderFilter] = useState('All');
  const [categoryFilter, setCategoryFilter] = useState('All');
  const [page, setPage] = useState(1);

  // Sync searchTerm state with URL query param when it changes (e.g. from nav bar)
  useEffect(() => {
    if (queryParam !== searchTerm) {
      setSearchTerm(queryParam);
    }
  }, [queryParam]);

  const genders = ['All', 'male', 'female', 'unisex'];
  const categories = ['All', 'designer', 'niche', 'budget'];

  const filteredPerfumes = useMemo(() => {
    const q = searchTerm.toLowerCase().trim();
    return PERFUME_DATABASE.filter(p => {
      const notes = Array.isArray(p.notes) ? p.notes : [];
      const matchesSearch = !q
        || (p.name || '').toLowerCase().includes(q)
        || (p.brand || '').toLowerCase().includes(q)
        || notes.some(n => (n || '').toLowerCase().includes(q));
      const matchesCategory = categoryFilter === 'All' || p.price_category === categoryFilter;
      const matchesGender = genderFilter === 'All' || p.gender === genderFilter;
      return matchesSearch && matchesCategory && matchesGender;
    });
  }, [searchTerm, categoryFilter, genderFilter]);

  // Properly reset page with useEffect (not useMemo)
  useEffect(() => {
    setPage(1);
  }, [searchTerm, categoryFilter, genderFilter]);

  const totalPages = Math.ceil(filteredPerfumes.length / ITEMS_PER_PAGE);
  const currentChunk = filteredPerfumes.slice((page - 1) * ITEMS_PER_PAGE, page * ITEMS_PER_PAGE);

  const counts = useMemo(() => ({
    all: PERFUME_DATABASE.length,
    designer: PERFUME_DATABASE.filter(p => p.price_category === 'designer').length,
    niche: PERFUME_DATABASE.filter(p => p.price_category === 'niche').length,
    budget: PERFUME_DATABASE.filter(p => p.price_category === 'budget').length,
    male: PERFUME_DATABASE.filter(p => p.gender === 'male').length,
    female: PERFUME_DATABASE.filter(p => p.gender === 'female').length,
    unisex: PERFUME_DATABASE.filter(p => p.gender === 'unisex').length,
  }), []);

  const startItem = filteredPerfumes.length === 0 ? 0 : (page - 1) * ITEMS_PER_PAGE + 1;
  const endItem = Math.min(page * ITEMS_PER_PAGE, filteredPerfumes.length);

  return (
    <div className="encyclopedia-container animate-fade-in">
      <div className="ency-header">
        <h1 className="ency-title serif-text">The Grimoire of Scents</h1>
        <p className="ency-subtitle">
          Browse {PERFUME_DATABASE.length} world-class fragrances by brand, note, vibe, or gender.
        </p>

        {/* Search Bar */}
        <div className="search-bar-container glass-panel">
          <span className="search-icon">🔍</span>
          <input
            type="text"
            id="grimoire-search"
            className="ency-search"
            placeholder="Search by name, brand, or note (e.g. 'Vanilla', 'Dior')..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
          {searchTerm && (
            <button
              className="search-clear-btn"
              onClick={() => setSearchTerm('')}
              aria-label="Clear search"
            >
              ✕
            </button>
          )}
        </div>

        {/* Gender Filter */}
        <div className="filter-tags" style={{ marginBottom: '0.75rem' }}>
          {genders.map(g => (
            <button
              key={g}
              className={`filter-btn ${genderFilter === g ? 'active' : ''}`}
              onClick={() => setGenderFilter(g)}
            >
              {g === 'All' ? `All (${counts.all})` : `${g.charAt(0).toUpperCase() + g.slice(1)} (${counts[g] || 0})`}
            </button>
          ))}
        </div>

        {/* Category Filter */}
        <div className="filter-tags">
          {categories.map(cat => (
            <button
              key={cat}
              className={`filter-btn ${categoryFilter === cat ? 'active' : ''}`}
              onClick={() => setCategoryFilter(cat)}
            >
              {cat === 'All' ? `All Tiers` : `${cat.charAt(0).toUpperCase() + cat.slice(1)} (${counts[cat] || 0})`}
            </button>
          ))}
        </div>
      </div>

      <div className="pagination-info" style={{ textAlign: 'center', marginBottom: '2rem', color: 'var(--text-secondary)' }}>
        Showing {startItem}–{endItem} of <strong style={{ color: 'var(--accent)' }}>{filteredPerfumes.length}</strong> elixirs
      </div>

      <div className="cards-grid ency-grid">
        {currentChunk.length > 0 ? (
          currentChunk.map(p => <PerfumeCard key={p.id} perfume={p} />)
        ) : (
          <div className="no-results">
            <p>No elixirs found matching "{searchTerm}".</p>
            <button className="btn btn-outline" style={{ marginTop: '1rem' }} onClick={() => { setSearchTerm(''); setGenderFilter('All'); setCategoryFilter('All'); }}>
              Clear Filters
            </button>
          </div>
        )}
      </div>

      {totalPages > 1 && (
        <div className="pagination-controls" style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '1rem', marginTop: '3rem' }}>
          <button className="btn btn-outline" disabled={page === 1} onClick={() => setPage(p => p - 1)}>
            ← Previous
          </button>
          <span style={{ color: 'var(--text-secondary)' }}>Page <strong style={{ color: 'var(--accent)' }}>{page}</strong> of {totalPages}</span>
          <button className="btn btn-outline" disabled={page === totalPages} onClick={() => setPage(p => p + 1)}>
            Next →
          </button>
        </div>
      )}
    </div>
  );
}

export default Encyclopedia;
