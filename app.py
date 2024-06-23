import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import fitz  
import logging
import mimetypes
import uvicorn
import sys
import cohere

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

# Initialize the cohere client with your API key
co = cohere.Client(api_key='CfPKJpnLJ2gKQDGlE8craNF0r05A9FXKlDtllcFv')

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

uploaded_pdf_text = ""

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        global uploaded_pdf_text  

        file_mime_type, _ = mimetypes.guess_type(file.filename)
        if file_mime_type != "application/pdf":
            raise HTTPException(status_code=400, detail="Please upload a PDF file.")
        
        for existing_file in os.listdir("uploaded_files"):
            file_path = os.path.join("uploaded_files", existing_file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        
        file_location = f"uploaded_files/{file.filename}"
        with open(file_location, "wb") as f:
            f.write(await file.read())

        new_text = extract_text_from_pdf(file_location)

        if not new_text.strip():
            raise HTTPException(status_code=400, detail="Extracted text is empty. Please upload a valid PDF.")

        uploaded_pdf_text = new_text

        return JSONResponse(content={"message": "PDF uploaded successfully"})

    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class QuestionRequest(BaseModel):
    question: str

@app.post("/answer-questions/")
async def answer_questions(request: QuestionRequest):
    try:
        global uploaded_pdf_text
        
        if not uploaded_pdf_text.strip():
            raise HTTPException(status_code=400, detail="No PDF text available. Please upload a PDF first.")
        
        try:
            message = f"""
            ## Instructions
            Answer the question based on the text below.

            ## Question
            {request.question}

            ## Input Text
            {uploaded_pdf_text}
            """
            response = co.chat(
                message=message,
                model="command-r-plus",
                temperature=0.3
            )
            answer = response.text.strip()
            return JSONResponse(content={"answer": answer})
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to get answer. Please try again with a different question. {str(e)}")

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
