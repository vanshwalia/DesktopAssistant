
import os
import pyttsx3
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
      speak("good morning sir!")

    elif hour>=12 and hour<18:
        speak("good afternoon sir")

    else:
        speak("good evening sir")  

    speak("i am jarvis and i am here to help you ")      

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

        try:
            print("Recognizing...")
            query=r.recognize_google(audio,language='en-in')
            print("User said : ",query)
        except Exception:
            #print(e)
            print("say that again please...")
            return "None" 
        return query



if __name__ == "__main__":
          
           while True:
           #if 1:
                
                query=takeCommand().lower()


                if 'wikipedia' in query:
                    speak("Searching Wikipedia...")
                    query=query.replace("wikipedia","")
                    results=wikipedia.summary(query,sentences=2)
                    speak("according to wikipedia")
                    print(results)
                    speak(results)

                    
                elif ('hello' or  'jarvis') in query:
                    wishMe()

                elif 'open youtube' in query:
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    webbrowser.open("google.com")

                elif 'open stackverflow' in query:
                    webbrowser.open("stackoverflow.com")   

                elif "what is the time" in query:
                    strTime=datetime.datetime.now().strftime("%H:%M")
                    speak(f"sir ,the time is{strTime}")

                elif "open code" in query:
                    codePath="C:\\Users\\VANSH WALIA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
                    os.startfile(codePath)
                    
                elif "open sublime" in query:
                      codePath="C:\\Program Files\\Sublime Text 3\\sublime_text.exe" 
                      os.startfile(codePath) 

                elif "open spotify" in query:
                      codePath="C:\\Users\\VANSH WALIA\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe" 
                      os.startfile(codePath)

                    