from googletrans import Translator
import eel

def translate(text,dest,src):
    tr = Translator()
    translated = tr.translate(text,dest=dest,src=src)
    eel.view_log_js(translated.text)