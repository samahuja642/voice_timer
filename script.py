from pip import main
import speech_recognition as sr
# import pyaudio
import pyttsx3
import time
from playsound import playsound
from os import system

def GetInput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio))
        command = r.recognize_google(audio)
    except sr.UnknownValueError:
        print('Unable To UnderStand')
        command = ''
    except sr.RequestError as e:
        print('Google Says error: {}'.format(e))
        command = ''
    finally:
        return command

def getWords(sentence):
    ls = []
    temp = ''
    for i in sentence:
        if(i==' '):
            ls.append(temp)
            temp = ''
        else:
            temp = ''.join((temp,i))
    ls.append(temp)
    return ls

def find(ls,str):
    count = 0
    for i in ls:
        if(i==str):
            return count
        count+=1
    return -1

def getAppropriate(words,str):
    if(find(words,str)==-1 and find(words,str[0:-1])==-1):
        return 0
    elif find(words,str)!=-1 and find(words,str[0:-1])==-1:
        return int(words[find(words,str)-1])
    elif find(words,str)==-1 and find(words,str[0:-1])!=-1:
        return int(words[find(words,str[0:-1])-1])
    else:
        return max(int(words[find(words,str)-1]),int(words[find(words,str[0:-1])-1]))

def countdown(t):
    while(t):
        mins,secs = divmod(t,60) 
        hour , mins = divmod(mins,60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hour,mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1
    print('Timer Completed!')

engine = pyttsx3.init()
engine.say("Hi Samarth Brother")
engine.runAndWait()
print('Say Something!')
command = GetInput()
if('timer' in command or 'reminder' in command):
    words = getWords(command)
    if('reminder' in command):
        engine.say("What should i remind you?")
        engine.runAndWait()
        remind_me = GetInput()
        hours = getAppropriate(words,'hours')
        minutes = getAppropriate(words,'minutes')
        seconds = getAppropriate(words,'seconds')
        total_time = hours*60*60 + minutes*60 + seconds
        countdown(total_time)
        engine.say(remind_me)
        engine.runAndWait()
    else:
        hours = getAppropriate(words,'hours')
        minutes = getAppropriate(words,'minutes')
        seconds = getAppropriate(words,'seconds')
        total_time = hours*60*60 + minutes*60 + seconds
        countdown(total_time)
        playsound('sound.mp3')
else:
    print('Wrong Command!')
engine.say('Signing Off!')
engine.runAndWait()
