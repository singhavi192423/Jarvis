import pyttsx3 
import speech_recognition as sr
import datetime 
import os
import webbrowser
import random
from requests import get
import wikipedia
import pywhatkit as kit
import sys
import pyjokes





engine =pyttsx3.init('sapi5')   # (sapi5) provide engine which is used for speak function
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#convert voice to text
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        audio =r.listen(source,phrase_time_limit=5)

    try:
        print("recognizing....")
        query= r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except:
        pass
    return query

def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning sir")
    if hour>12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening")
    speak("hello sir i m jarvis , what can i do  for you")





if __name__=="__main__":
    wishme()
    while True:

        query= takecommand().lower()
        print(query)


        if "hello jarvis" in query:
            helloans=("hello sir",'hello budyy','namaste','ram ram','hello avinash and shivam','hello enginners','hello rawalians')
            speak(random.choice(helloans))

        elif 'how are  you jarvis' in query:
            howans=("i am good  what about you",'bdhiya h g app btao','i m feeling low charge me','apna kaam krr dimag kharab mt krr ')
            speak(random.choice(howans))

        elif "how was your day jarvis" in query:
            speak("well its so exhausting, please don't give me any another work,but for you i am always available")

        elif 'what is your favourite food' in query:
            speak("for me elctricity is my favourite food, by the way whats your favourite food")

        elif 'i love banana' in query:
            speak("are you a monkey, i m just joking its good for your health")

        elif 'you are the best person jarvis' in query:
            speak("i am not a person , i am a machine ")

        elif 'can you do some work for me' in query:
            speak("just give me orders sir")

        elif "open notepad" in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
            
        
        elif 'open command prompt' in query:
            cpath="C:\\Users\\Ankit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools"
            os.startfile(cpath)

        elif "play music" in query:
            music_dir="C:\\music"
            songs = os.listdir(music_dir)
            rd=random.choice(songs)
            #for songs in songs:
             #   if song.endswith('mp3'):
            os.startfile(os.path.join(music_dir,rd))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")

        
        elif "what is my ip address" in query:
            ip= get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")


        elif 'who is' in query:
            person = query.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            speak(info)


        elif 'what is the' in query:
            meaning = query.replace('what is the meaning', '')
            result = wikipedia.summary(meaning,1)
            print(result)
            speak(result)
        

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif 'open stack overflow' in query:
            webbrowser.open("www.stackoverflow.com")


        elif "open google" in query:
            speak("sir,what should i search for you on google")
            cm=takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "send message on whatsapp" in query:
            kit.sendwhatmsg("+917290969224", "sos i need help",23,30)

        elif "play song on youtube" in query:
            kit.playonyt("song")

        elif "play something on youtube" in query:
            kit.playonyt("videos")

        elif "set alarm" in query:
            nn=int(datetime.datetime.now().hour())
            if nn==6:
                music_dir="C:\\music"
                songs = os.listdir(music_dir)
                rd=random.choice(songs)
                os.startfile(os.path.join(music_dir,rd))

        elif "tell me a joke" in query:
            joke=pyjokes.get_joke() 
            speak(joke)
            print(joke)


        elif "no thanks" in query:
            speak("thank you sir for using me ,have a good day ")
            sys.exit()

        elif "shutdown system" in query:
            os.system("shutdown /s /t 5")


            speak ('do you want to ask something else')