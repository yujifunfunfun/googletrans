import eel
import trans

@eel.expose
def translate(text,dest,src):
    trans.translate(text,dest,src)

eel.init('template')
eel.start('index.html')