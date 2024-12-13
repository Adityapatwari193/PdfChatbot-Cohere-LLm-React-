# PDF Question-Answering System

This project is a **PDF Question-Answering System** that extracts text from a PDF file, uploads it to the server, and allows users to ask questions about the content. The system uses **FastAPI** for the backend and **React** for the frontend. Additionally, it integrates **Cohere's language model** for generating answers to questions.

---

## Features

1. **Upload PDF**: Users can upload a PDF file.
2. **Extract Text**: Text is extracted from the uploaded PDF using the PyMuPDF library.
3. **Ask Questions**: Users can ask questions about the uploaded PDF content.
4. **AI-Powered Answers**: The backend processes the question using Cohere's language model and provides an answer.
5. **Interactive UI**: A dynamic, user-friendly React frontend to interact with the system.


## Technologies Used

### Backend
- **FastAPI**: Handles API endpoints and request processing.
- **PyMuPDF (fitz)**: Extracts text from PDF files.
- **Cohere API**: Processes user questions and generates AI-powered answers.
- **uvicorn**: Runs the FastAPI server.

### Frontend
- **React**: Dynamic frontend with interactive components.
- **Axios**: Handles API requests to the backend.

### Others
- **CORS Middleware**: Enables secure cross-origin requests.

---

## Setup Instructions

Follow these steps to set up the project on your local system:

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm (Node Package Manager)
- A Cohere API Key ([Get one here](https://cohere.ai/))

### Backend Setup

1. Clone the repository:
   ```bash
   https://github.com/Adityapatwari193/PdfChatbot-Cohere-LLm-React-
   cd pdf-question-answering/backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Replace the placeholder Cohere API key in the `main.py` file:
   ```python
   co = cohere.Client(api_key='your-cohere-api-key')
   ```

5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the `frontend` folder:
   ```bash
   cd ../frontend
   ```

2. Install the required npm packages:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

4. Open your browser and navigate to `http://localhost:3000`.

---

## API Endpoints

### Upload PDF
- **Endpoint**: `/upload-pdf/`
- **Method**: `POST`
- **Description**: Accepts a PDF file, extracts its text, and stores it for future questions.

### Answer Questions
- **Endpoint**: `/answer-questions/`
- **Method**: `POST`
- **Description**: Accepts a question and returns an AI-generated answer based on the uploaded PDF's content.

---

## Folder Structure

```
root
├── backend
│   ├── main.py          # FastAPI backend implementation
│   ├── requirements.txt # Backend dependencies
├── frontend
│   ├── src
│   │   ├── App.js       # React main component
│   │   ├── Header.js    # Header component
│   │   ├── App.css      # Styles
├── screenshots          # Folder for screenshots
```

---

## Screenshots

### Upload PDF Screen
![Upload Screen](https://raw.githubusercontent.com/Adityapatwari193/PdfChatbot-Cohere-LLm-React-/main/screenshots/Screenshot%202024-12-13%20203827.png)

### Question and Answer Screen
![Q&A Screen](https://raw.githubusercontent.com/Adityapatwari193/PdfChatbot-Cohere-LLm-React-/main/screenshots/Screenshot%202024-12-13%20203909.png)

---
