# PDF Question-Answering System

This project is a **PDF Question-Answering System** that extracts text from a PDF file, uploads it to the server, and allows users to ask questions about the content. The system uses **FastAPI** for the backend and **React** for the frontend. Additionally, it integrates **Cohere's language model** for generating answers to questions.

---

## Features

1. **Upload PDF**: Users can upload a PDF file.
2. **Extract Text**: Text is extracted from the uploaded PDF using the PyMuPDF library.
3. **Ask Questions**: Users can ask questions about the uploaded PDF content.
4. **AI-Powered Answers**: The backend processes the question using Cohere's language model and provides an answer.
5. **Interactive UI**: A dynamic, user-friendly React frontend to interact with the system.

---

## Screenshots

### Upload PDF Screen
![Upload Screen](https://raw.githubusercontent.com/Adityapatwari193/PdfChatbot-Cohere-LLm-React-/main/screenshots/upload_screen.png)

### Question and Answer Screen
![Q&A Screen](https://raw.githubusercontent.com/Adityapatwari193/PdfChatbot-Cohere-LLm-React-/main/screenshots/qa_screen.png)

---

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
   git clone https://github.com/your-username/pdf-question-answering.git
   cd pdf-question-answering/backend
