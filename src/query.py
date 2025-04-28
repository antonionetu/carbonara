import model, translate


def find_answer(question, table):
    prompt = f"""
        You are a chatbot that only returns the answer, with a title only.

        Given the table below:
        {table.to_string(index=False)}

        Answer the following question:
        {translate.pt_to_en(question)}
    """
    return model.LLM.query(prompt.strip())
