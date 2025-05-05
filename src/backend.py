from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from typing import List
import asyncio
from googletrans import Translator

import query, builder, utils


app = FastAPI()
translator = Translator()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def translate_to_en(text: str) -> str:
    translated = await translator.translate(text, src='pt', dest='en')
    return translated.text


@app.post("/generate-chart")
async def main(
    files: List[UploadFile] = File(...),
    question: str = Form(...),
    kind_of_chart: str = Form(...)
):
    dfs = [utils.uploadFileToPandas(f) for f in files]
    if not dfs or any(df is None for df in dfs):
        return JSONResponse(status_code=400, content={"error": "Nenhum arquivo foi válido."})

    translated_question = await translate_to_en(question)
    answer = await query.find_answer(translated_question, dfs)
    html_chart = await builder.create_chart(answer.text, kind_of_chart)

    return HTMLResponse(content=html_chart.text, status_code=200)
