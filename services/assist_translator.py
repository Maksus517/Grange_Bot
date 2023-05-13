from googletrans import Translator


def text_translator(text: str, src: str, dest: str):
    try:
        translator = Translator()
        translation = translator.translate(text=text, src=src, dest=dest)
        return translation.text

    except Exception as ex:
        return ex
