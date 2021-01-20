import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Chandan Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Chandan Sir")
    else:
        speak("Good Evening Chandan Sir")

    speak("I am your assistance . Please tell me how can i help you")


def takeCommand():
    # It takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query

# def sendEmail(to,content):
#     server = smtplib.SMTP('smtp.gmail.com',587)
#     server.ehlo()
#     server.starttls()
#     server.login('chandansunil7839@gmail.com', 'maurya7839')
#     server.sendmail('chandansunil7839@gmail.com' ,to, content)
#     server.close()


if __name__ == "__main__":
    # speak("chandan is a good boy")
    wishMe()
    # if 1:
    while True:
        query = takeCommand().lower()

    # Logic for executing task based on query
        if 'wikipedia' in query:

            speak('Searching Wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
           webbrowser.open("youtube.com")

        elif 'open google' in query:
           webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
           webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'E:\Music\Music'
            songs= os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f" The time is {strTime}")
            speak(f'Sir, the time is {strTime}')

        elif 'open code' in query:
            codePath= "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'who are you' in query:
            speak('i am Chandan assistant and work for him')

        elif 'who is mohit' in query:
            speak('mohit is my friend')

        elif 'who is sunil' in query:
            speak('sunil is Chandan brother')

        elif 'who is vikash' in query:
            speak('vikash is Chandan friend')

        elif 'Who is your developer' in query:
            speak('Mr. Chandan has developed me.')

        elif 'do you believe in god' in query:
            speak('Yes, because my developer is equivalent to god to me.')
        # elif 'email to sunil' in query:
        #     try:
        #         speak('what should i say ?')
        #         content = takeCommand()
        #         to = 'pcslancer@gmail.com'
        #         sendEmail(to,content)
        #         speak("Email has been sent")
        #     except Exception as e:
        #         print(e)
        #         speak("sorry chandan bro , email was not sent")
