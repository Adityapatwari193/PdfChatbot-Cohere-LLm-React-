PDF Chatbot using Cohere LLM and React

This project is a chatbot system that allows users to interact with a PDF document through natural language queries. It leverages the Cohere LLM (Large Language Model) to understand user questions and retrieve relevant content from the PDF files. The system utilizes React for the frontend, providing a seamless and responsive user interface, while the backend processes PDF documents to extract text and handle conversational responses.

The key functionality of this project includes:

Uploading PDF files.
Processing and indexing the text content of the PDFs.
Allowing users to ask questions about the PDF content.
Using Cohere LLM to generate meaningful responses based on the text data.
A clear and interactive user interface built with React. 

Setup 

Prerequisites:
Before setting up the project, ensure you have the following installed on your system:

Node.js (Version 14.x or higher)
npm or yarn (For managing frontend dependencies)
Python 3.x (For the backend environment)
Cohere API key (Sign up at Cohere to get your API key for accessing the LLM)

Setup Instructions:
1.Clone the repository:

git clone https://github.com/Adityapatwari193/PdfChatbot-Cohere-LLm-React.git
cd PdfChatbot-Cohere-LLm-React

2.Install dependencies for the frontend (React):

npm install

3.Add your Cohere API key:

Create a .env file in the backend directory and add your Cohere API key
COHERE_API_KEY=your_cohere_api_key_here

4.Run the backend server:

python app.py

5.Run the frontend (React):
npm start

6.Access the application:

Open your browser and go to http://localhost:3000 to interact with the PDF chatbot.

How the Project Works:
PDF Upload: Users can upload a PDF document through the interface. The PDF content is extracted and processed by the backend.

Querying: After uploading the PDF, users can ask natural language questions about the content. The chatbot interface allows seamless interaction.

Response Generation: The backend uses the Cohere LLM to process the user's query, search for relevant sections within the PDF content, and generate responses.

Frontend: The frontend is built using React, making the interface dynamic and interactive. It handles file uploads, sends user queries to the backend, and displays the responses.
