PDF Chatbot using Cohere LLM and React

This project is a chatbot system that allows users to interact with a PDF document through natural language queries. It leverages the Cohere LLM (Large Language Model) to understand user questions and retrieve relevant content from the PDF files. The system utilizes React for the frontend, providing a seamless and responsive user interface, while the backend processes PDF documents to extract text and handle conversational responses.

Key Features

PDF Upload: Users can upload PDF files.

Text Processing: The backend processes and indexes the text content of the PDFs.

Query Support: Users can ask questions about the PDF content.

Cohere LLM: Generates meaningful responses based on the text data.

Interactive UI: A clear and dynamic interface built with React.

Setup

Prerequisites

Before setting up the project, ensure you have the following installed on your system:

Node.js (Version 14.x or higher)

npm or yarn (For managing frontend dependencies)

Python 3.x (For the backend environment)

Cohere API Key (Sign up at Cohere to get your API key for accessing the LLM)

Installation Steps

Clone the repository:

git clone https://github.com/Adityapatwari193/PdfChatbot-Cohere-LLm-React.git
cd PdfChatbot-Cohere-LLm-React

Install frontend dependencies (React):

npm install

Add your Cohere API key:

Navigate to the backend directory.

Create a .env file and add your Cohere API key:

COHERE_API_KEY=your_cohere_api_key_here

Run the backend server:

python app.py

Run the frontend (React):

npm start

Access the application:

Open your browser and navigate to:

http://localhost:3000

Interact with the PDF chatbot from the user interface.

How the Project Works

1. PDF Upload

Users can upload a PDF document through the interface. The PDF content is extracted and processed by the backend.

2. Querying

After uploading the PDF, users can ask natural language questions about its content. The chatbot interface allows seamless interaction.

3. Response Generation

The backend uses the Cohere LLM to process user queries, search for relevant sections within the PDF content, and generate accurate responses.

4. Frontend

The frontend is built using React, ensuring a dynamic and interactive experience. It handles file uploads, sends user queries to the backend, and displays the responses effectively.

Enjoy interacting with your PDFs using the PDF Chatbot!
