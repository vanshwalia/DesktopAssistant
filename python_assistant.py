import sys
import os
import pyttsx3 
import datetime
import wikipedia
import webbrowser
import speech_recognition as sr


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

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

    speak("i am your python assistant and i am here to help you ")      

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


def end_program():
     sys.exit()
    
        



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

                    
                elif ('hello' or  'python' or "python assistant") in query:
                    wishMe()

                elif 'open youtube' in query:
                    webbrowser.open("https://www.youtube.com")
                    speak("youtube is opened")

                elif 'open google' in query:
                    webbrowser.open("https://www.google.com")
                    speak("google opened ")

                elif 'open stackverflow' in query:
                    webbrowser.open("https://www.stackoverflow.com") 
                    speak("stackoverflow opened")  

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
                      codePath="C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.162.583.0_x86__zpdnekdrzrea0\\spotify.exe" 
                      os.startfile(codePath)

                elif "open whatsapp" in query:
                      codePath="C:\\Program Files\\WindowsApps\\5319275A.WhatsAppDesktop_2.2123.8.0_x64__cv1g1gvanyjgm\\app\\whatsapp.exe" 
                      os.startfile(codePath)


                elif "exit"or"end" in query:
                    end_program()      

                    