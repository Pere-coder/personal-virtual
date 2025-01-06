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
            # we add listeing so we know when its listening
            print("Listening...") 
            r.adjust_for_ambient_noise(source2, duration=0.5)
            r.pause_threshold = 2
            audio2 = r.listen(source2)

            #we do need interneet connection for this recognize_google 
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say: " , MyText)

            #the brains of some sort...or at least it does some bit of thinking
            response = get_prompts(MyText)
            speakText(response)
    except sr.RequestError as e:
        print(f"could not process results, {e}")
    except sr.UnknownValueError:
        print("unknown error occurred")
