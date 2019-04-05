from gtts import gTTS
import os

tts = gTTS(text="Would you like a spot of tea?", lang='en-uk')
tts.save("pcvoice.mp3")
os.system("start pcvoice.mp3")