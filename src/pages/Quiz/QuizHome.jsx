import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './QuizHome.css';

function QuizHome({ setTheme }) {
  const navigate = useNavigate();
  const [homeSearch, setHomeSearch] = useState('');

  const handleHomeSearch = (e) => {
    e.preventDefault();
    if (homeSearch.trim()) {
      navigate(`/encyclopedia?q=${encodeURIComponent(homeSearch.trim())}`);
    }
  };

  const handleGenderSelect = (gender) => {
    // Set global theme based on gender
    if (gender === 'male') {
      setTheme('male');
    } else if (gender === 'female') {
      setTheme('female');
    } else {
      setTheme(''); // Unisex / default can be basic dark
    }
    
    // Pass gender directly in state explicitly to avoid race conditions
    navigate('/quiz', { state: { gender } });
  };

  return (
    <div className="quiz-home-container animate-fade-in">
      <div className="hero-content glass-panel">
        <div className="decoration corner-tl"></div>
        <div className="decoration corner-br"></div>
        <h1 className="hero-title heading-gold">Discover Your Aura</h1>
        <p className="hero-subtitle serif-text">
          Scent is the most powerful memory. Which shadow do you cast?
        </p>

        <div className="home-search-section">
          <p className="search-instruction serif-text">Looking for something specific?</p>
          <form className="home-search-form" onSubmit={handleHomeSearch}>
            <input 
              type="text" 
              className="home-search-input" 
              placeholder="Search by brand, name or note..."
              value={homeSearch}
              onChange={(e) => setHomeSearch(e.target.value)}
            />
            <button type="submit" className="home-search-submit">
              Search the Grimoire
            </button>
          </form>
        </div>

        <div className="divider-container">
          <span className="divider-label serif-text">OR START THE RITUAL</span>
        </div>

        <div className="gender-selection">
          <button 
            className="btn btn-outline gender-btn male-btn" 
            onClick={() => handleGenderSelect('male')}
          >
            Man
          </button>
          
          <button 
            className="btn btn-outline gender-btn female-btn" 
            onClick={() => handleGenderSelect('female')}
          >
            Woman
          </button>

          <button 
            className="btn btn-outline gender-btn unisex-btn" 
            onClick={() => handleGenderSelect('unisex')}
          >
            Unisex
          </button>
        </div>
      </div>
    </div>
  );
}

export default QuizHome;
