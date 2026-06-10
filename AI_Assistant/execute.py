import text_to_speech
import speech_text
import datetime
import webbrowser

user_data = speech_text.speech_to_txt()
if "what is your name" in user_data:
    text_to_speech.text_to_speech("My name is virtual assistant")
    
elif "hi" in user_data or "hello" in user_data or "how are you" in user_data:
    text_to_speech.text_to_speech("Hello, how can I be of assistance today?")
    
elif "thank you" in user_data or "thanks" in user_data:
    text_to_speech.text_to_speech("You are welcome, do you need help with anything else?")
    
elif "current time" in user_data or "time now" in user_data:
    current_time = datetime.datetime.now()
    Time = (str)(current_time) + "Hour :", (str)(current_time.minute) + "Minute"
    text_to_speech.text_to_speech(Time)
    
elif "shutdown" in user_data:
     text_to_speech.text_to_speech("Shutting down now")
     
elif "play music" in user_data:
    webbrowser.open("https://open.spotify.com/")
    text_to_speech.text_to_speech("Playing music on spotify.com")
    
elif "open youtube" in user_data:
    webbrowser.open("https://www.youtube.com/")
    text_to_speech.text_to_speech("Opening youtube ...")
    
elif "open google" in user_data:
    webbrowser.open("https://www.google.com/")
    text_to_speech.text_to_speech("Opening google ...")
    

else:
    text_to_speech.text_to_speech("I execute the command")
    
    
    
    