import asyncio
from googletrans import Translator


async def translate(text, lang_src, lang_dest):
    translator = Translator()
    translated_text = await translator.translate(text, src=lang_src, dest=lang_dest)
    return translated_text.text


def pt_to_en(pt_text):
    return asyncio.run(translate(pt_text, 'pt', 'en'))


def en_to_pt(en_text):
    return asyncio.run(translate(pt_text, 'en', 'pt'))
