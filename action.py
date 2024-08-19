import text_to_speech
import speech_to_text
import datetime
import weather
import webbrowser

def action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        response = "My name is Aether"
    elif "hello" in user_data or "hi" in user_data:
        response = "Hi Sir! How can I help you?"
    elif "good morning" in user_data:
        response = "Good morning, sir!"
    elif "time now" in user_data:
        current_time = datetime.datetime.now()
        response = f"The current time is {current_time.hour} Hour : {current_time.minute} Minute"
    elif "shut down" in user_data:
        response = "Okay sir!"
    elif "play music" in user_data:
        webbrowser.open("https://youtube.com/")
        response = "Music is ready for you!"
    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        response = "Google is ready for you!"
    elif "weather" in user_data:
        response = weather.weather()
    else:
        response = "I'm not able to understand!"

    # Pass the response to text_to_speech and return it
    text_to_speech.text_to_speech(response)
    return response
