import speech_recognition as sr

def speech_to_text():
    
    r = sr.Recognizer()

   
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source)  
        
        print("Listening for speech...")
        audio = r.listen(source)  

    try:
        print("Recognizing speech...")
        voice_data = r.recognize_google(audio)
        print(f"Recognized Text: {voice_data}")
        return voice_data

    except sr.UnknownValueError:
        
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
      
        print(f"Could not request results from Google Speech Recognition service; {e}")

speech_to_text()
