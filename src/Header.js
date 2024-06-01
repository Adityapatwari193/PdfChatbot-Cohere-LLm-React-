import React, { useState } from 'react';
import axios from 'axios';
import './Header.css'; 

function Header() {
  const [fileName, setFileName] = useState('');

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file) {
      try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await axios.post('http://localhost:8000/upload-pdf/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        if (response.status === 200) {
          setFileName(file.name);
          alert('PDF uploaded successfully!');
        }
      } catch (error) {
        console.error('Failed to upload PDF', error);
        alert('Failed to upload PDF');
      }
    }
  };

  return (
    <>
      <header className="header">
        <nav className="navbar">
          <div className="navbar-content">
            <img src={`${process.env.PUBLIC_URL}/aiplanet.png`} alt="Logo" className="navbar-logo" />
            <span className="logo-text">planet</span>
            <input
              type="file"
              accept="application/pdf"
              onChange={handleFileChange}
              style={{ display: 'none' }}
              id="upload-input"
            />
            <button className="upload-button" onClick={() => document.getElementById('upload-input').click()}>
              <span className="plus-symbol">+</span> Upload PDF
            </button>
          </div>
        </nav>
      </header>
      {fileName && <h2 className="file-name-display">Ask anything relating to {fileName}</h2>}
    </>
  );
}

export default Header;
