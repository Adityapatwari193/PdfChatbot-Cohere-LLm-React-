<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PDF Chatbot using Cohere LLM and React</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0;
      padding: 0 20px;
    }
    h1, h2, h3 {
      color: #333;
    }
    pre {
      background-color: #f4f4f4;
      padding: 10px;
      border-radius: 5px;
      overflow-x: auto;
    }
    code {
      background-color: #f4f4f4;
      padding: 2px 4px;
      border-radius: 3px;
    }
    ul {
      margin: 10px 0;
      padding: 0 20px;
    }
    a {
      color: #007acc;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    hr {
      border: 0;
      border-top: 1px solid #ccc;
      margin: 20px 0;
    }
  </style>
</head>
<body>
  <h1>PDF Chatbot using Cohere LLM and React</h1>
  <p>
    This project is a chatbot system that allows users to interact with a PDF document through natural language queries. 
    It leverages the Cohere LLM (Large Language Model) to understand user questions and retrieve relevant content from the PDF files. 
    The system utilizes React for the frontend, providing a seamless and responsive user interface, while the backend processes PDF documents 
    to extract text and handle conversational responses.
  </p>

  <h2>Key Features</h2>
  <ul>
    <li><strong>PDF Upload:</strong> Users can upload PDF files.</li>
    <li><strong>Text Processing:</strong> The backend processes and indexes the text content of the PDFs.</li>
    <li><strong>Query Support:</strong> Users can ask questions about the PDF content.</li>
    <li><strong>Cohere LLM:</strong> Generates meaningful responses based on the text data.</li>
    <li><strong>Interactive UI:</strong> A clear and dynamic interface built with React.</li>
  </ul>
  <hr>

  <h2>Setup</h2>

  <h3>Prerequisites</h3>
  <p>Before setting up the project, ensure you have the following installed on your system:</p>
  <ul>
    <li><strong>Node.js</strong> (Version 14.x or higher)</li>
    <li><strong>npm</strong> or <strong>yarn</strong> (For managing frontend dependencies)</li>
    <li><strong>Python 3.x</strong> (For the backend environment)</li>
    <li><strong>Cohere API Key</strong> (Sign up at <a href="https://cohere.ai" target="_blank">Cohere</a> to get your API key for accessing the LLM)</li>
  </ul>

  <h3>Installation Steps</h3>
  <ol>
    <li><strong>Clone the repository:</strong>
      <pre><code>git clone https://github.com/Adityapatwari193/PdfChatbot-Cohere-LLm-React.git
cd PdfChatbot-Cohere-LLm-React</code></pre>
    </li>
    <li><strong>Install frontend dependencies (React):</strong>
      <pre><code>npm install</code></pre>
    </li>
    <li><strong>Add your Cohere API key:</strong>
      <ul>
        <li>Navigate to the backend directory.</li>
        <li>Create a <code>.env</code> file and add your Cohere API key:</li>
      </ul>
      <pre><code>COHERE_API_KEY=your_cohere_api_key_here</code></pre>
    </li>
    <li><strong>Run the backend server:</strong>
      <pre><code>python app
