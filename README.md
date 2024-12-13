# PDF Question & Answering System

This project is a **PDF Question & Answering System** that allows users to upload PDF files, extract text, and ask questions related to the content of the uploaded PDF. The system leverages **FastAPI** for the backend, **Cohere API** for text processing, and a React-based frontend for an intuitive user experience.

---

## Features

- **PDF Upload**: Upload PDF files directly from the browser.
- **Text Extraction**: Extracts text from the uploaded PDF for processing.
- **Question Answering**: Ask questions related to the PDF content, powered by Cohere's NLP model.
- **User-Friendly Interface**: Intuitive React-based interface for uploading PDFs and asking questions.

---

## Tech Stack

### Backend
- **FastAPI**: A modern, fast web framework for building APIs.
- **Cohere API**: Used for generating answers to user questions.
- **PyMuPDF (fitz)**: For extracting text from PDFs.
- **Python**: The programming language for the backend.
- **CORS Middleware**: For enabling cross-origin requests.

### Frontend
- **React**: A JavaScript library for building user interfaces.
- **Axios**: For making HTTP requests to the backend.
- **CSS**: For styling the UI.

---

## Setup Instructions

### Prerequisites

- **Node.js** (for the frontend)
- **Python 3.9+** (for the backend)
- **pip** (Python package installer)
- **Cohere API Key** (Sign up at [Cohere](https://cohere.ai) to get your API key)

### Backend Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-question-answering.git
   cd pdf-question-answering/backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Cohere API key:
   - Open the backend file and replace `CfPKJpnLJ2gKQDGlE8craNF0r05A9FXKlDtllcFv` with your own Cohere API key.

5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

   The backend will be available at `http://localhost:8000`.

### Frontend Setup

1. Navigate to the frontend folder:
   ```bash
   cd ../frontend
   ```

2. Install the dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

   The frontend will be available at `http://localhost:3000`.

---

## Usage

1. Launch both the backend and frontend servers.
2. Open the React application in your browser (`http://localhost:3000`).
3. Upload a PDF file using the "Upload PDF" button.
4. Ask questions related to the uploaded PDF in the text input area.
5. View the answers in the "Questions and Answers" section.

---

## File Structure

```plaintext
pdf-question-answering
├── backend
│   ├── main.py          # FastAPI backend implementation
│   ├── requirements.txt # Backend dependencies
│   └── uploaded_files   # Directory for storing uploaded PDFs
└── frontend
    ├── src
    │   ├── App.js       # Main React component
    │   ├── Header.js    # Header component for PDF upload
    │   └── App.css      # Styling for the app
    └── public
        ├── question.png # Question icon
        ├── aiplanet.png # Logo icon
```

---

## API Endpoints

### `/upload-pdf/`
- **Method**: POST
- **Description**: Uploads a PDF and extracts its text.
- **Request Body**: PDF file (multipart/form-data)
- **Response**: `{ "message": "PDF uploaded successfully" }`

### `/answer-questions/`
- **Method**: POST
- **Description**: Accepts a question and returns an answer based on the uploaded PDF.
- **Request Body**:
  ```json
  {
      "question": "Your question here"
  }
  ```
- **Response**:
  ```json
  {
      "answer": "Generated answer from Cohere API"
  }
  ```

---

## Screenshots

### Main Interface
![Main Interface](public/screenshot-main.png)

### PDF Upload
![PDF Upload](public/screenshot-upload.png)

### Question & Answer
![Question & Answer](public/screenshot-qa.png)

---

## Known Issues

- Ensure the PDF contains extractable text (not scanned images).
- Only one PDF can be processed at a time; uploading a new PDF will overwrite the previous one.

---

## Future Enhancements

- Support for processing multiple PDFs.
- Addition of OCR capabilities for scanned PDFs.
- Improved error handling and detailed feedback.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## Contact

For any questions or issues, please contact [your-email@example.com].
