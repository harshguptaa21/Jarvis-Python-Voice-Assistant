import speech_recognition as sr  #instead of writing speech_recognition we can write sr
import webbrowser
import pyttsx3 # to convert text to speech
import musicLibrary
import requests
import ollama
import os
from dotenv import load_dotenv
#pip install pocketsphinx



recognizer = sr.Recognizer()
engine = pyttsx3.init()
load_dotenv()
newsapi = os.getenv("NEWSDATA_API_KEY")

def speak(text):
    # print("Speak function called:", text)
    # engine.say(text)
    # engine.runAndWait()
    # print("Finished speaking")

    print("Jarvis speaking:", text)
    try:
        voice_engine = pyttsx3.init("sapi5")
        voice_engine.setProperty("rate", 160)
        voice_engine.setProperty("volume", 1.0)
        voice_engine.say(text)
        voice_engine.runAndWait()
        voice_engine.stop()
        del voice_engine
    except Exception as e:
        print("Speech error:", repr(e))

# Ollama AI function
def askJarvis(question):
    try:
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Jarvis, a helpful voice assistant. "
                        "Give simple, concise answers."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        answer = response.message.content
        print("Jarvis:", answer)
        speak(answer)

    except Exception as e:
        print("Ollama error:", e)
        speak("Sorry, I could not answer that.")


def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link= musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(
            "https://newsdata.io/api/1/latest",
            params={
                "apikey": newsapi,
                "country": "in",
                "language": "en"
            }
        )

        if r.status_code == 200:
            data = r.json()
            articles = data.get("results", [])

            for article in articles[:5]:
                title = article.get("title")
                if title:
                    print(title)
                    speak(title)
        else:
            print("Error fetching news:", r.status_code)

    else:
        #Let open AI handles the request the ai code is written in client.py
        askJarvis(c)
        
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer() 
        print("recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print("Wake word detected:", repr(word))

            if(word.lower().strip() == "jarvis"):
                print("Step 1: Wake word matched")
                speak("How can i help you")
                print("Step 2: Speech function completed")

                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                command = r.recognize_google(audio)
                print("Recognized command:", command)

                processCommand(command)
        except Exception as e:
            print("Error;{0}".format(e))
    
