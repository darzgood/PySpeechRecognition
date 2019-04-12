import os

from gtts import gTTS
import os

tts = gTTS(text="Would you like a spot of tea?", lang='en')
tts.save("pcvoice.mp3")

def mp3gen():
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                yield os.path.join(root, filename)

def saveName(name, filename):
    tts = gTTS(text=name, lang='en')
    name = "{0}(Name) - {1}.mp3".format(filename, name)
    tts.save(name)
    print(name)

def main():                
    for mp3file in mp3gen():
        parts = mp3file[2:].split(" - ")
        if len(parts) == 3:
            saveName(parts[1], parts[0])
            
if __name__ == "__main__":
    main()