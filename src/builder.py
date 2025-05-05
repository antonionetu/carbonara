import pandas as pd
import model, translate


async def create_chart(answer, kind="bar"):
    translated_kind = await translate.pt_to_en(kind)

    prompt = f"""
    You are a developer specialized in generating only pure HTML and CSS, with no explanations or comments.

    Instructions:
    - Return only the HTML and CSS code, and NOTHING else.
    - If there is any text in English, translate it into Brazilian Portuguese (pt-BR).
    - Generate a maximum of 10 items in the chart.
    - Use only HTML and CSS (no JavaScript).
    - Create a "{translated_kind}" type chart that represents the provided data.
    - Return the code all together
    - Also dont return "```"
    - Attention, the background is already black, so create colorful background chart.

    Data:
    {answer}
    """

    chart = await model.LLM.builder(prompt.strip())
    return chart
