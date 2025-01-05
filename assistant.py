import speech_recognition as sr
import pyttsx3
from searchbot import get_prompts

r = sr.Recognizer()

def speakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()



while (1):
    try:
        with sr.Microphone() as source2:
            print("Listening...")
            r.adjust_for_ambient_noise(source2, duration=0.2)
            r.pause_threshold = 2
            audio2 = r.listen(source2)
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say: "+MyText)
            talk_to_ollama = get_prompts(MyText)
            speakText(talk_to_ollama)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    
    except sr.UnknownValueError:
        print("unknown error occured")