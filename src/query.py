import model, translate


async def find_answer(question, tables):
    tables_content = [t.to_string(index=False) for t in tables]
    translated_question = await translate.pt_to_en(question)
    
    prompt = f"""
        You are a chatbot that only returns the answer, with a title only.

        Given the table(s) below:
        {tables_content}

        Answer the following question:
        {translated_question}
    """

    answer = await model.LLM.query(prompt.strip())
    return answer
