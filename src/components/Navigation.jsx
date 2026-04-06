import React, { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import './Navigation.css';

function Navigation({ theme }) {
  const location = useLocation();
  const navigate = useNavigate();
  const [query, setQuery] = useState('');

  const handleSearch = (e) => {
    e.preventDefault();
    if (query.trim()) {
      // Navigate to encyclopedia with a search query param
      navigate(`/encyclopedia?q=${encodeURIComponent(query.trim())}`);
      setQuery('');
    }
  };

  return (
    <nav className="navbar glass-panel">
      <div className="decoration corner-tl"></div>
      <div className="decoration corner-br"></div>
      <div className="nav-brand">
        <Link to="/">
          <h1 className="logo-text">Obsidian Aura</h1>
        </Link>
      </div>

      {/* Global Search */}
      <form className="nav-search-form" onSubmit={handleSearch}>
        <div className="nav-search-wrapper">
          <span className="nav-search-icon">🔍</span>
          <input
            type="text"
            className="nav-search-input"
            placeholder="Search perfumes..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            aria-label="Global perfume search"
          />
          {query && (
            <button
              type="button"
              className="nav-search-clear"
              onClick={() => setQuery('')}
              aria-label="Clear"
            >
              ✕
            </button>
          )}
        </div>
      </form>

      <div className="nav-links">
        <Link
          to="/"
          className={`nav-link ${location.pathname === '/' || location.pathname === '/quiz' ? 'active' : ''}`}
        >
          The Oracle
        </Link>
        <Link
          to="/encyclopedia"
          className={`nav-link ${location.pathname === '/encyclopedia' ? 'active' : ''}`}
        >
          The Grimoire
        </Link>
      </div>
    </nav>
  );
}

export default Navigation;
