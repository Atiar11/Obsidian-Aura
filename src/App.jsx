import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Navigation from './components/Navigation';
import QuizHome from './pages/Quiz/QuizHome';
import QuizEngine from './pages/Quiz/QuizEngine';
import Results from './pages/Quiz/Results';
import Encyclopedia from './pages/Encyclopedia';

function App() {
  const [theme, setTheme] = useState(''); // '' (default), 'male', 'female'

  // Apply theme to body
  useEffect(() => {
    document.body.className = theme ? `theme-${theme}` : '';
  }, [theme]);

  return (
    <Router>
      <div className="app-container">
        {/* Foolproof Physical Live Wallpaper */}
        <div className="live-wallpaper">
          <div className="mesh-blob blob-1"></div>
          <div className="mesh-blob blob-2"></div>
          <div className="mesh-blob blob-3"></div>
        </div>
        
        <Navigation theme={theme} />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<QuizHome setTheme={setTheme} />} />
            <Route path="/quiz" element={<QuizEngine theme={theme} />} />
            <Route path="/results" element={<Results theme={theme} />} />
            <Route path="/encyclopedia" element={<Encyclopedia />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
