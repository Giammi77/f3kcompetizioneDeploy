# THIS MODULE MUST BE INSTALLED ON SERVER VIA PIP
from gtts import gTTS
def create_voice(message,path):
    ttmp3=gTTS(message)
    ttmp3.save(path)
