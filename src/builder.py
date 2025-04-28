import pandas as pd
import model, translate


def create_chart(answer, kind="bar"):
    prompt = f"""
    You are a developer specialized in generating only pure HTML and CSS, with no explanations or comments.

    Instructions:
    - Return only the HTML and CSS code, and NOTHING else.
    - If there is any text in English, translate it into Brazilian Portuguese (pt-BR).
    - Generate a maximum of 10 items in the chart.
    - Use only HTML and CSS (no JavaScript).
    - Create a "{translate.pt_to_en(kind)}" type chart that represents the provided data.
    - Return the code all together
    - Also dont return "```"

    Data:
    {answer}
    """
    return model.LLM.builder(prompt.strip())
