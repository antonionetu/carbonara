from googletrans import Translator


async def translate(text, lang_src, lang_dest):
    translator = Translator()
    translated_text = await translator.translate(text, src=lang_src, dest=lang_dest)
    return translated_text.text

async def pt_to_en(pt_text):
    return await translate(pt_text, 'pt', 'en')

async def en_to_pt(en_text):
    return await translate(en_text, 'en', 'pt')
