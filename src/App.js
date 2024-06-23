import React, { useState } from 'react';
import './App.css'; 
import Header from './Header.js';
import axios from 'axios';

function App() {
  const [text, setText] = useState('');
  const [questionsAndAnswers, setQuestionsAndAnswers] = useState([]);
  const [errorMessage, setErrorMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!text.trim()) {
      setErrorMessage('Please enter a question.');
      return;
    }

    setIsLoading(true); 

    try {
      const response = await axios.post('http://localhost:8000/answer-questions/', {
        question: text.trim()
      });

      if (response.data && response.data.answer) {
        const newQuestionAndAnswer = {
          question: text.trim(),
          answer: response.data.answer
        };

        setQuestionsAndAnswers([...questionsAndAnswers, newQuestionAndAnswer]);

        setText(''); 
        setErrorMessage('');
      } else {
        setErrorMessage('Failed to get answer. Please try again later.');
      }
    } catch (error) {
      console.error('Failed to submit question', error);
      setErrorMessage('Failed to submit question. Please try again later.');
    } finally {
      setIsLoading(false); 
    }
  };

  return (
    <div className="app-container">
      <Header />
      <div className="content">
        {errorMessage && <p className="error-message">{errorMessage}</p>}
        {questionsAndAnswers.map((qa, index) => (
          <div key={index} className="question-and-answer">
            <p className="question"><img src={`${process.env.PUBLIC_URL}/question.png`} alt="Logo" className="question-logo" /> {qa.question}</p>
            <p className="answer"> <img src={`${process.env.PUBLIC_URL}/aiplanet.png`} alt="Logo" className="answer-logo" /> {qa.answer}</p>
            <br></br>
          </div>
        ))}
      
      </div>
      <form className="textarea-form" onSubmit={handleSubmit}>
        <div className="textarea-container">
          <textarea
            className="textarea"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Type your question here..."
          ></textarea>
          <button type="submit" className="submit-button">
            {isLoading ? <span className="spinner"></span> : <span>➤</span>}
          </button>
        </div>
      </form>
    </div>
  );
}

export default App;
