import datetime
import random
from urllib.parse import SplitResult
import speech_recognition as sr
import pyttsx3 
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id )

def speak ( audio):
    engine.say(audio) # this basically process the audio 
    engine.runAndWait() # we will come to here this when this command run


# wishing command 

def wish ():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12 :
        speak("good morning sir,how can i help you")
    elif hour >= 12 and hour < 18 :
        speak('good afternoon sir, hows you ')
    else :
        speak('good evening sir')

def takeCommand(): # it takes microphone input from user and return as string output

    r = sr.Recognizer()
    with sr.Microphone() as source :

        print("i'm listing...")
        r.pause_threshold = 0.8
        # r.energy_threshold = 300
        # r.phrase_threshold = 0.1
        audio = r.listen(source)


        try :
            print("Recogniging...")
            query = r.recognize_google(audio,language= 'en-in')
            print(f'user said : { query } \n')

        except Exception as e :
            # print(e)     error messege 
            print('sorry ! could you please say that again')
            return "None"
        return query

if __name__ == "__main__" :
    speak('welcome back sir')
    # wish()
    
    while True :
        query = takeCommand().lower()

        # -----*** writing thhe logic for operations***---
        
        if "wikipedia" in query :
            speak('ok sir searching on wikipedia')
            query = query.replace('wikipedia','')
            result = wikipedia.summary(query, sentences = 1)
            speak('accordung to wikipedia')
            print(result)
            speak(result)

        elif 'open youtube' in query : 
            speak ('sure sir')
            webbrowser.open("youtube.com")

        elif 'open google' in query :
            speak('on the way sir')
            webbrowser.open('google.com')

        elif 'open stack overflow' in query:
            speak('ok boss')
            webbrowser.open('stackoverflow.com')

        elif 'see you later' in query :
            l = ['do let me know,   when you need somthing', 'ok sir,  call me whenever you need somthing', 'happy to serve you','always remember im just a call away,  sir']
            speak(random.choice(l))
            quit()

        elif " father of your boss" in query :
            speak('mister sarfaraj ansari is your father, with the dashing personality ')

        elif 'mother of your boss' in query:
            speak('gulista ansari is your mother such a beautiful lady with a kind heart')

        elif 'my mother' in query :
            speak('gulista ansari is your mother such a beautiful lady with a kind heart')

        elif 'my father' in query :
            speak('mister sarfaraj ansari is your father, with the dashing personality ')

        elif 'who is your boss' in query :
            l = ['aman ansari is my boss', " you are the one im here to serve always", 'the person whome i love the most,  i care about him the most and that is you']
            speak(random.choice(l))

        elif  "you are working very fine" in query :
            l = ['thank you sir' , 'anything to meke you smile', 'always there to give my best', 'only here to serve you sir']
            speak(random.choice(l))

        elif 'wake up jarvis' in query :
            speak("always attentive to serve you ,  sir") 

        elif 'your name' in query :
            speak('i am,  jarvis,  a personal assistance of, aman  ansari')  

        elif "who are you" in query :
            l = ['i am virtual personoal assistance of the, aman ansri ', 'my name is jarvis, i am an idea into the reality']
            speak(random.choice(l))

        elif "what are you doing" in query:
            l = ["trying to be better,  sir", 'thinking, what are you thinking, sir','nothing much,  sir']  
            speak(random.choice(l))

        elif 'who am i' in query :
            l = ['you are my beloved person,  you are one and only my sir, i am allowed to call, aman, ansari', 'your name is aman', 'you are the one who created me','jo apni herogiri, kabhi nahi chhodta']
            speak(random.choice(l))   

        elif 'my name' in query :
            l = ['you are my beloved person,  you are one and only my sir, i am allowed to call, aman, ansari', 'your name is aman', 'you are the one who created me','jo apni herogiri, kabhi nahi chhodta']
            speak(random.choice(l))   

        elif 'your birthday' in query :
            l = ['i was designed on,  16th of the july in the evening',"16 july was that auspicious day for me",'16 july  was the day when my boss  converted his idea into me '] 
            speak(random.choice(l))

        elif "hug me" in query:
            speak('i wish i could hug you, i would realy love to come into the reality')   

        elif "who is your father" in query :
            l = ['aman,  ansari is the one who designed me', 'my one and only hero, aman ansari'] 
            speak(random.choice(l))
        else :
            speak('i am really sorry to dissapoint you,  this is not in my knowledge')
            