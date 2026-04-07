import React, { useMemo } from 'react';
import { useLocation, Navigate, useNavigate } from 'react-router-dom';
import { getRecommendations } from '../../utils/recommendationEngine';
import './Results.css';

// Defined OUTSIDE the component so it never causes unmount/remount on re-render
const PerfumeCard = ({ perfume, navigate }) => {
  const vibes = Array.isArray(perfume.vibe) ? perfume.vibe : [];
  const occasions = Array.isArray(perfume.occasion) ? perfume.occasion : [];
  const notes = Array.isArray(perfume.notes) ? perfume.notes : [];
  
  // Calculate a human-readable match percentage or label based on matchCount
  const matchPercent = Math.min(Math.round((perfume.matchCount / 5) * 100), 100);
  let matchLabel = "Strong Match";
  if (matchPercent === 100) matchLabel = "Perfect Aura Match";
  else if (matchPercent < 80) matchLabel = "Close Match";

  return (
    <div className="perfume-card glass-panel">
      <div className="decoration corner-tl"></div>
      <div className="decoration corner-br"></div>
      <div className="perfume-img-container">
        <div className={`match-badge ${matchPercent === 100 ? 'perfect' : ''}`}>
          {matchLabel} ({matchPercent}%)
        </div>
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
        <div className="perfume-price">{perfume.price_range}</div>
        <p className="perfume-desc">{perfume.description}</p>
        <div className="perfume-stats">
          <div className="stat">
            <span className="stat-label">Gender:</span>
            <span className="stat-value" style={{ textTransform: 'capitalize' }}>{perfume.gender}</span>
          </div>
          {vibes.length > 0 && (
            <div className="stat">
              <span className="stat-label">Vibe:</span>
              <span className="stat-value">{vibes.join(', ')}</span>
            </div>
          )}
          {notes.length > 0 && (
            <div className="stat">
              <span className="stat-label">Notes:</span>
              <span className="stat-value">{notes.slice(0, 4).join(', ')}</span>
            </div>
          )}
          <div className="stat">
            <span className="stat-label">Longevity:</span>
            <span className="stat-value">{perfume.longevity || 'N/A'} ({perfume.wearing_time || 'N/A'})</span>
          </div>
          <div className="stat">
            <span className="stat-label">Performance:</span>
            <span className="stat-value">{perfume.performance || 'N/A'}</span>
          </div>
          {occasions.length > 0 && (
            <div className="stat">
              <span className="stat-label">Occasion:</span>
              <span className="stat-value">{occasions.join(', ')}</span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

function Results() {
  const location = useLocation();
  const navigate = useNavigate();
  const preferences = location.state?.preferences;

  // Always compute recommendations (hooks must not be inside conditionals)
  const recommendations = useMemo(
    () => preferences ? getRecommendations(preferences) : { niche: [], designer: [], budget: [] },
    [preferences]
  );

  if (!preferences) {
    return <Navigate to="/" replace />;
  }

  const noResults =
    recommendations.niche.length === 0 &&
    recommendations.designer.length === 0 &&
    recommendations.budget.length === 0;

  return (
    <div className="results-container animate-fade-in">
      <div className="results-header">
        <h2 className="results-title serif-text">Your Aura Unleashed</h2>
        <p className="results-subtitle">Based on your desires, the Oracle has spoken.</p>
        <button className="btn btn-outline" onClick={() => navigate('/encyclopedia')}>
          Browse The Grimoire Instead
        </button>
      </div>

      {noResults && (
        <div style={{ textAlign: 'center', padding: '4rem', color: 'var(--text-secondary)' }}>
          <p style={{ fontSize: '1.3rem', marginBottom: '1rem' }}>No matching scents found for your profile.</p>
          <p>Try broadening your preferences or choosing different vibes.</p>
          <button className="btn btn-primary" style={{ marginTop: '2rem' }} onClick={() => navigate('/')}>
            Retry the Oracle
          </button>
        </div>
      )}

      {recommendations.niche.length > 0 && (
        <div className="price-tier">
          <h3 className="tier-title serif-text">The Exquisite (Niche &amp; Luxury)</h3>
          <div className="cards-grid">
            {recommendations.niche.map(p => <PerfumeCard key={p.id} perfume={p} navigate={navigate} />)}
          </div>
        </div>
      )}

      {recommendations.designer.length > 0 && (
        <div className="price-tier">
          <h3 className="tier-title serif-text">The Classics (Designer)</h3>
          <div className="cards-grid">
            {recommendations.designer.map(p => <PerfumeCard key={p.id} perfume={p} navigate={navigate} />)}
          </div>
        </div>
      )}

      {recommendations.budget.length > 0 && (
        <div className="price-tier">
          <h3 className="tier-title serif-text">The Hidden Gems (Budget)</h3>
          <div className="cards-grid">
            {recommendations.budget.map(p => <PerfumeCard key={p.id} perfume={p} navigate={navigate} />)}
          </div>
        </div>
      )}

      {!noResults && (
        <div className="restart-action">
          <button className="btn btn-primary" onClick={() => navigate('/')}>Consult the Oracle Again</button>
        </div>
      )}
    </div>
  );
}

export default Results;
