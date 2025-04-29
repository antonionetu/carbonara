from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import List

import query, builder, utils

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate-chart")
async def main(
    files: List[UploadFile] = File(...),
    question: str = Form(...),
    kind_of_chart: str = Form(...)
):
    files = [utils.uploadFileToPandas(f) for f in files]
    print("FIles: ", files)
    if not files:
        return {
            "error": "Nenhum arquivo foi válido."
        }
    
    answer = query.find_answer(question, files)
    html_chart = builder.create_chart(answer, kind_of_chart)
    
    return {
        "question": question,
        "answer": answer,
        "chart": html_chart,
    }
