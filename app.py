import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
import fitz  
import logging
import mimetypes
import uvicorn
import sys

app = FastAPI()

# Enable CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Create the 'uploaded_files' directory if it doesn't exist
if not os.path.exists("uploaded_files"):
    os.makedirs("uploaded_files")

# Load multiple question answering models for answering
qa_pipeline1 = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
qa_pipeline2 = pipeline("question-answering", model="deepset/roberta-base-squad2")
qa_pipeline3 = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Load the summarization pipeline
summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")


def post_process_answer(answer):
    sentences = answer.split(".")
    filtered_sentences = [sentence.strip() for sentence in sentences if len(sentence.strip()) > 10]
    processed_answer = ". ".join(filtered_sentences)
    return processed_answer

# Function to combine multiple answers without repetition
def combine_answers(answers):
    unique_answers = list(dict.fromkeys(answers))  
    combined_answer = " ".join(unique_answers)
    return combined_answer

# Function to get answers from multiple models and combine them
def get_combined_answer(question, context):
    if not context.strip():
        raise ValueError("Context cannot be empty")
    answers = []
    for qa_pipeline in [qa_pipeline1, qa_pipeline2, qa_pipeline3]:
        try:
            answer = qa_pipeline(question=question, context=context)["answer"]
            processed_answer = post_process_answer(answer)
            answers.append(processed_answer)
        except Exception as e:
            logging.warning(f"QA model failed: {e}")
            continue
    
    if not answers:
        raise ValueError("Failed to get answers from all models")
    
    combined_answer = combine_answers(answers)
    return combined_answer

# Function to extract text from a PDF file 
def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as pdf:
            logging.info(f"Number of pages in the PDF: {pdf.page_count}")
            for page_num in range(len(pdf)):
                page = pdf[page_num]
                page_text = page.get_text("text")  
                if isinstance(page_text, list):
                    page_text = " ".join(page_text)  
                text += page_text
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from PDF: {str(e)}")
    return text

# Variable to store the extracted text
uploaded_pdf_text = ""

#Api endpoint to upload a pdf file
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        global uploaded_pdf_text  # Use the global variable for storing extracted text

        # Checking if a file is a pdf or not
        file_mime_type, _ = mimetypes.guess_type(file.filename)
        if file_mime_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Please upload a PDF file.")
        
        # Delete existing files in the uploaded_files directory
        for existing_file in os.listdir("uploaded_files"):
            file_path = os.path.join("uploaded_files", existing_file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        # Save the new file
        file_location = f"uploaded_files/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())

        new_text = extract_text_from_pdf(file_location)

        if not new_text.strip():
            raise HTTPException(status_code=400, detail="Extracted text is empty. Please upload a valid PDF.")

        # Clear the stored text data and update with new text
        uploaded_pdf_text = new_text

        return JSONResponse(content={"message": "PDF uploaded successfully"})

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


class QuestionRequest(BaseModel):
    question: str

#Api endpoint to upload questions and get answers
@app.post("/answer-questions/")
async def answer_questions(request: QuestionRequest):
    try:
        global uploaded_pdf_text  
        
        if not uploaded_pdf_text.strip():
            raise HTTPException(status_code=400, detail="No PDF text available. Please upload a PDF first.")
        
        # Check if the user input contains the word "summary"
        if "summary" in request.question.lower():
            # Generate a summary of the text
            try:
                summary = summarization_pipeline(uploaded_pdf_text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
                return JSONResponse(content={"answer": summary})
            except IndexError:
                raise HTTPException(status_code=500, detail="Failed to generate summary. Please try again with a different PDF.")
        else:
            # Get combined answer from multiple models
            combined_answer = get_combined_answer(request.question, uploaded_pdf_text)
            return JSONResponse(content={"answer": combined_answer})

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    try:
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except KeyboardInterrupt:
        logging.info("Server shutdown gracefully.")
