import text_to_speech
import speech_text
import datetime
import webbrowser
import weather

def execute(data):
    user_data = data.lower()
    
    if "what is your name" in user_data:
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"
        
    elif "hi" in user_data or "hello" in user_data or "how are you" in user_data:
        text_to_speech.text_to_speech("Hello, how can I be of assistance today?")
        return "Hello, how can I be of assistance today?"
        
    elif "thank you" in user_data or "thanks" in user_data:
        text_to_speech.text_to_speech("You are welcome, do you need help with anything else?")
        return "You are welcome, do you need help with anything else?"
        
    elif "current time" in user_data or "time now" in user_data:
        current_time = datetime.datetime.now()
        Time = (str)(current_time) + "Hour :", (str)(current_time.minute) + "Minute"
        text_to_speech.text_to_speech(Time)
        return Time 
        
    elif "shutdown" in user_data:
        text_to_speech.text_to_speech("Shutting down now")
        return "Shutting down now"
        
    elif "play music" in user_data:
        webbrowser.open("https://open.spotify.com/")
        text_to_speech.text_to_speech("Playing music on spotify.com")
        return "Playing music on spotify.com"
        
    elif "open youtube" in user_data:
        webbrowser.open("https://www.youtube.com/")
        text_to_speech.text_to_speech("Opening youtube ...")
        return "Opening youtube ..."
        
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com/")
        text_to_speech.text_to_speech("Opening google ...")
        return "Opening google ..."
        
    elif "weather" in user_data:
        weather_app = weather.weather()
        text_to_speech.text_to_speech(weather_app)
        return weather_app
        

    else:
        text_to_speech.text_to_speech("I cannot execute the command")
        return "I cannot execute the command"
        
        
        
    