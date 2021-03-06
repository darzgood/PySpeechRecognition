import speech_recognition as sr


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.

    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("'recognizer' must be 'Recognizer' instance")
    if not isinstance(microphone, sr.Microphone):
        raise TypeError("'microphone' must be 'Microphone' instance")
    
    with microphone as source:
        print("A moment of silence please...")
        recognizer.adjust_for_ambient_noise(source)
        print("Okay, begin talking.")
        audio = recognizer.listen(source)
        
    response = {"success":True, "error":None, "transcription":None}
    
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"
        
    return response
    
if __name__ == "__main__":
    
    r = sr.Recognizer()
    m = sr.Microphone()
    
    response = recognize_speech_from_mic(r, m)
    if response["error"] == None:
        print(response["transcription"])
    else:
        print(response["error"])