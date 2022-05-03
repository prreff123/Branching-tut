import webbrowser
import pyttsx3
import speech_recognition as sr
# import PyAudio
import datetime
import wikipedia
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. Please tell me how may I help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query 

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587) 
    server.ehlo()
    server.starttls()
    server.login('priyanshujain09062003@gmail.com','your-password')
    server.sendmail('priyanshujain09062003@gmail.com',to,content)
    server.close()   

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'python documentation' in query:
            webbrowser.open("pyhon documentation")    

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir, the time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\asus\\Downloads\\Python Course"
            os.startfile(codepath)

        elif 'email to PJ' in query:
            try:
                speak("What should I say")
                content = takecommand()
                to = "priyanshujain09062003@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("sorry my friend PJ bhai. I am not able to send this email")