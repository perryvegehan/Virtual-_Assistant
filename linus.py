import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
# first of all we need a speak function
engine=pyttsx3.init('sapi5')

voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)
newVoiceRate = 175
engine.setProperty('rate',newVoiceRate)

#SPEAK---> This function speaks a given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#WISHME---> starts the program. wishes the user
def wishMe():
    hour=int (datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good Morning Mr. Narain")
    elif(hour>12 and hour<=17):
        speak("Good Afternoon Mr. Narain")

    else:
        speak("Good Evening Mr. Narain")
   # speak("I am Lyna, your virtual assistant.")

   # speak("Initializing...")
    #speak("Final authentication pending")
    speak("You can call me Schneizel and I am at your command sir.")


#Take command--> takes voice commands and returns string output
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)
    try:
        print("Processing....")
        query=r.recognize_google(audio,language="en-in")
        print(query)
    except Exception:
        print("Sorry! Say that again please...")
        return "None"
    return query

# EMAIL FUnCTION
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('pratyushnarain55555@gmail.com','penndragon')
    server.sendmail('pratyushnarain55555@gmail.com',to,content)
    server.close()

# MAIN
if __name__=="__main__":

    wishMe()
    query=takeCommand().lower()

    # Logic for executing the tasks:
    if 'code 0 0 0 3 0 0 3' in query:
        speak("Preparing for standby mode")
        speak("standby mode activated")
    if 'wikipedia' in query:
        speak("searching in wikipedia")
        query=query.replace('wikipedia',"")
        wiki_result=wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        speak(wiki_result)
    elif 'open youtube' in query or'youtube' in query:
        speak("Opening youtube")
        webbrowser.get('windows-default').open('https://youtube.com')
    elif 'open a website' in query or 'website' in query or 'search' in query:
        speak("Please tell me which website should I open")
        website=takeCommand().lower()
        from googlesearch import search

        for j in search(website, tld="co.in", num=1,start=1,stop=1, pause=2):
            print(j)
            webbrowser.get('windows-default').open(j)

        speak("Performing an internet search")

    elif 'time' in query:
        strtime=datetime.datetime.now().strftime('%H:%M:%S')
        speak(f"Sir, the time is {strtime}")
    elif 'notepad' in query:
        speak("opening notepad")
        os.system("Notepad")
    elif 'email' in query:
        speak('Email sender activated')
        speak("What will be the content?")
        content = takeCommand().lower()
        to = '500060673@stu.upes.ac.in'
        sendEmail(to, content)
        speak("Your email has been sent Sir!")
    elif 'shut' in query or 'shut down' in query or 'turn off' in query:
        speak("Do you really want to turn off your machine??")
        speak("Speak yes to proceed and speak No to cancel")
        answer=takeCommand().lower()
        if answer=='yes':
            os.system("shutdown /s /t 1")
        else:
            speak("command aborted")









