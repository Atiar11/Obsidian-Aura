import React, { useState } from 'react';
import { useLocation, useNavigate, Navigate } from 'react-router-dom';
import { VIBES, OCCASIONS, POWERS, CONTEXTS, PSYCHOLOGIES } from '../../data/perfumeDatabase';
import './QuizEngine.css';

const QUIZ_STEPS = [
  {
    id: 'vibe',
    title: 'The Olfactory Profile',
    subtitle: 'Which aura do you wish to project? (Select up to 2)',
    options: VIBES
  },
  {
    id: 'occasion',
    title: 'The Functional Purpose',
    subtitle: 'Where does this scent belong? (Select up to 2)',
    options: OCCASIONS
  },
  {
    id: 'power',
    title: 'The Performance',
    subtitle: 'What matters most in your sillage? (Select up to 2)',
    options: POWERS
  },
  {
    id: 'context',
    title: 'The Environment',
    subtitle: 'In what context will you wear this? (Select up to 2)',
    options: CONTEXTS
  },
  {
    id: 'psychology',
    title: 'The Drivers',
    subtitle: 'What is the ultimate goal of your fragrance? (Select 1)',
    options: PSYCHOLOGIES,
    singleChoice: true
  }
];

function QuizEngine() {
  const location = useLocation();
  const navigate = useNavigate();
  
  // Need to ensure gender was selected, if not redirect to home
  const gender = location.state?.gender;

  const [currentStep, setCurrentStep] = useState(0);
  const [preferences, setPreferences] = useState({
    gender: gender || 'unisex',
    vibe: [],
    occasion: [],
    power: [],
    context: [],
    psychology: []
  });

  if (!gender) {
    return <Navigate to="/" replace />;
  }

  const stepData = QUIZ_STEPS[currentStep];

  const handleOptionToggle = (option) => {
    setPreferences(prev => {
      const currentList = prev[stepData.id];
      let newList = [...currentList];
      
      if (newList.includes(option)) {
        newList = newList.filter(item => item !== option);
      } else {
        if (stepData.singleChoice) {
          newList = [option];
        } else if (currentList.length < 2) {
          newList.push(option);
        }
      }
      return { ...prev, [stepData.id]: newList };
    });
  };

  const handleNext = () => {
    if (currentStep < QUIZ_STEPS.length - 1) {
      setCurrentStep(curr => curr + 1);
    } else {
      // Finished quiz! Navigate to results
      navigate('/results', { state: { preferences } });
    }
  };

  const handleBack = () => {
    if (currentStep > 0) {
      setCurrentStep(curr => curr - 1);
    } else {
      navigate('/');
    }
  };

  return (
    <div className="quiz-container animate-fade-in">
      <div className="quiz-panel glass-panel">
        <div className="decoration corner-tl"></div>
        <div className="decoration corner-br"></div>
        
        <div className="progress-bar">
          <div 
            className="progress-fill" 
            style={{ width: `${((currentStep + 1) / QUIZ_STEPS.length) * 100}%` }}
          ></div>
        </div>

        <div className="quiz-header">
          <span className="step-indicator serif-text">Chapter {currentStep + 1} of {QUIZ_STEPS.length}</span>
          <h2 className="step-title">{stepData.title}</h2>
          <p className="step-subtitle">{stepData.subtitle}</p>
        </div>

        <div className="options-grid">
          {stepData.options.map(option => {
            const isSelected = preferences[stepData.id].includes(option);
            return (
              <button
                key={option}
                className={`option-btn ${isSelected ? 'selected' : ''}`}
                onClick={() => handleOptionToggle(option)}
              >
                {option}
              </button>
            )
          })}
        </div>

        <div className="quiz-actions">
          <button className="btn btn-outline" onClick={handleBack}>
            {currentStep === 0 ? 'Restart' : 'Back'}
          </button>
          <button 
            className="btn btn-primary" 
            onClick={handleNext}
            disabled={preferences[stepData.id].length === 0}
          >
            {currentStep === QUIZ_STEPS.length - 1 ? 'Reveal My Scents' : 'Continue'}
          </button>
        </div>

      </div>
    </div>
  );
}

export default QuizEngine;
