import pyttsx3
import speech_recognition as sr
import datetime
import os
#import cv2
import  random
from requests import get
import wikipedia
import webbrowser
#import pywhatkit as kit
import smtplib 
import sys
engine = pyttsx3.init('sapi5') # object creation
voices =engine.getProperty('voices')
#print(voices[1].id)
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)
#text to speech function
def speak(audio):
    engine.say(audio)
    print (audio)
    engine.runAndWait()
# speech to text
def takecommand():
     r =sr.Recognizer()
     with sr.Microphone() as source:
            print("Listening.....")
            r.pause_threshold =1
            audio = r.listen(source,timeout =1,phrase_time_limit= 5)
     try:
       print("Recongnizing......")
       query =r.recognize_google(audio,language='en-in')
       print(f" user said: {query} ")

     except Exception as e:
            speak("Say that again please......")
            return 'none'
     return query    
#Date time finder
def wish():
  hour =int(datetime.datetime.now().hour)
  if hour>=0 and  hour<=12:
           speak("good Morning")
  elif hour>=12 and  hour<=16:
        speak("Good Afternoon")
  elif hour>=16 and  hour<=24:
      speak("Good Evening")      
  else:
    speak("Good night")
  speak("I am Jarvis sir,Please tell me,how I can help you ")
# send Email
def sendEmail(to,content):
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.login('dr830691@gmail.com','Hypass@123')
      server.sendmail('dr830691@gmail.com',to,content)
      server.close()

      
if __name__ == "__main__":
      #takecommand()
      #speak("Hello Sir")
     wish()
     while True:
          query= takecommand().lower()
          #logic building for  task
          if 'open notepad' in query:
              npath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories"
              os.startfile(npath)
          if 'open Devcpp' in query:
                npath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Bloodshed Dev-C++"
                os.startfile(npath)
          if 'open command prompt' in query:
                os.system('start cmd')
          #if'open camera' in query:
           #     cap=cv2.VideoCaptur(0)
              #  while True:
               #       ret. img=cap.read()
                #      cv2.imshow('webcam',img)
                 #     k= cv2.waitKey(50)
                  #    if k==27:
                   #         break;
                #cap.release()
                #cv2.destroyAllWindows()
          elif 'play music' in query:
                 music_dir="E:\\music"
                 songs= os.listdir(music_dir)
                 #rd= random.choice(songs)
                 #os.startfile(os.path.join(music_dir,songs[0]))
                 #os.startfile(os.path.join(music_dir,rd))
                 for song in songs:
                       if song.endswith('.mp3'):
                             os.startfile(os.path.join(music_dir,song))
          elif 'ip address'  in query:
            ip =get('https://api.ipify.org').text
            speak(f"  your  ip address is {ip}")
          elif 'wikipedia' in query:
                speak("Searching wikipedia....")
                query = query.replace("wikipedia","")
                results=wikipedia.summary(query,sentences=5)
                speak("According to wikipedia")
                speak(results)
          elif 'open youtube' in query:
                webbrowser.open('www.youtube.com')
          elif 'open facebook' in query:
                webbrowser.open('www.facebook.com')
          elif 'open google' in query:
                speak("sir, what should i search o google")
                search= takecommand().lower()
                webbrowser.open(f"{search}")
          elif 'send message' in query:
                kit.sendwhatmsg("+919654960324","this is Ravindar message",16,24)    
          elif 'play  song on youtube' in query:
            kit.playanyt("TERE NAM") 
          elif 'email to dr' in query:
            try:
              speak("what should i say")
              content = takecommand().lower()
              to = 'dhesi1939@gmail.com'
              sendEmail(to,content)
              speak('Email has been sent to dr succesfully')
            except Exception as e:
               error =e
               print(error)
               speak(f'sorry sir,I cant send email right now due to the following reason {error}')
          elif "no thanks" in query:
                speak("Thanks for using me, sir,Have a good day.")
                sys.exit()
          speak("sir, Do you have any other work")        

               
