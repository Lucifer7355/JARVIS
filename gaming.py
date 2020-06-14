import subprocess 
import wolframalpha 
import pyttsx3 
import tkinter 
import json 
import random 
import operator 
import speech_recognition as sr 
import datetime 
import webbrowser 
import os 
import winshell 
import pyjokes
import wikipedia
import feedparser 
import smtplib 
import ctypes 
import time 
import requests 
import shutil 
from twilio.rest import Client 
from clint.textui import progress 
from ecapture import ecapture as ec 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen
from selenium import  webdriver
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time
import pyautogui
import psutil


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id)


def notifyMe(title,message):
  notification.notify(
    title = title,
    message = message,
    app_icon = "2750762.ico",
    timeout = 25
    )

def getData(url):
  r = requests.get(url)
  return r.text


def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 
  
def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    if hour>= 0 and hour<12: 
        speak("Good Morning Sir !") 
   
    elif hour>= 12 and hour<18: 
        speak("Good Afternoon Sir !")    
   
    else: 
        speak("Good Evening Sir !")   
   
    assname =("Jarvis 1 point o") 
    speak("I am your Assistant") 
    speak(assname) 
      
  
def usrname(): 
    speak("Hello Ankit its nice to see you") 
    uname = "ANKIT" 
    speak("Welcome Mister") 
    speak(uname) 
    columns = shutil.get_terminal_size().columns 
      
    print("#####################".center(columns)) 
    print("Welcome Mr.", uname.center(columns)) 
    print("#####################".center(columns)) 
      
    speak("How can i Help you, Sir") 
  
def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
        r.pause_threshold = 0.5
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Say that again please...")   
        return "None"
      
    return query 
   
def sendEmail(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
      
    # Enable low security in gmail 
    server.login('ankitviddya@gmail.com', 'Ankit@1234') 
    server.sendmail('ankitviddya@gmail.com', to, content) 
    server.close() 

if __name__ == '__main__': 
    clear = lambda: os.system('cls') 
      
    # This Function will clean any 
    # command before execution of this python file 
    clear() 
    wishMe() 
    usrname()
    speak("make sure you have a nice internet connection and specified modules of the source code to have a sweet talk with me")
      
    while True: 
          
        query = takeCommand().lower() 
          
        # All the commands said by user will be  
        # stored here in 'query' and will be 
        # converted to lower case for easily  
        # recognition of command 
        if 'wikipedia' in query: 
            speak('Searching Wikipedia...') 
            query = query.replace("wikipedia", "") 
            results = wikipedia.summary(query, sentences = 3) 
            speak("According to Wikipedia") 
            print(results) 
            speak(results) 
  
        elif 'open youtube' in query: 
            speak("Here you go to Youtube\n") 
            webbrowser.open("youtube.com") 
  
        elif 'open google' in query: 
            speak("Here you go to Google\n") 
            webbrowser.open("google.com") 
  
        elif 'open stackoverflow' in query: 
            speak("Here you go to Stack Over flow.Happy coding") 
            webbrowser.open("stackoverflow.com")    
  
        elif 'play music' in query or "play song" in query: 
            speak("Here you go with music") 
            # music_dir = "G:\\Song" 
            music_dir = "C:\\Users\\acer\\Downloads\\music"
            songs = os.listdir(music_dir) 
            print(songs)     
            random = os.startfile(os.path.join(music_dir, songs[1])) 
  
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")     
            print(f"Sir, the time is {strTime}")   
            speak(f"Sir, the time is {strTime}")
        
        elif 'screenshot' in query: 
            try:
              img = pyautogui.screenshot()
              img.save("E:\\aladin\\screenshots\\ss.png")
              speak("done sir!!")
            except:
              speak("could not take the screenshot sir")

        elif 'code blocks' in query: 
            codePath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codePath)

        elif 'cpu' in query: 
            usage = str(psutil.cpu_percent())
            speak("CPU is at"+usage)
            battery = psutil.sensors_battery()
            speak("Battery is at")
            speak(battery.percent)
            speak("percent")
  
        elif 'email to ankit' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                to = "ankitviddya@gmail.com"    
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'send a mail' in query: 
            try: 
                speak("What should I say?") 
                content = takeCommand() 
                speak("whome should i send") 
                to = input()     
                sendEmail(to, content) 
                speak("Email has been sent !") 
            except Exception as e: 
                print(e) 
                speak("I am not able to send this email") 
  
        elif 'how are you' in query: 
            speak("I am fine, Thank you") 
            speak("How are you, Sir") 
  
        elif 'fine' in query or "good" in query: 
            speak("It's good to know that your fine") 
  
        elif "change my name to" in query: 
            query = query.replace("change my name to", "") 
            assname = query 
  
        elif "change name" in query: 
            speak("What would you like to call me, Sir ") 
            assname = takeCommand() 
            speak("Thanks for naming me") 
  
        elif "what's your name" in query or "What is your name" in query: 
            speak("My friends call me") 
            speak(assname) 
            print("My friends call me", assname) 
  
        elif 'exit' in query: 
            speak("Thanks for giving me your time")
            speak("Jarvis going offline sir....") 
            exit() 
  
        elif "who made you" in query or "who created you" in query:
            print("I have been created by Ankit kumar srivastava.")
            speak("I have been created by Ankit kumar srivastava.") 
              
        elif 'joke' in query: 
            speak(pyjokes.get_joke()) 
              
        elif "calculate" in query:  
              
            app_id = "VKLUPR-96E5EX3V9L" 
            client = wolframalpha.Client(app_id) 
            indx = query.lower().split().index('calculate')  
            query = query.split()[indx + 1:]  
            res = client.query(' '.join(query))  
            answer = next(res.results).text 
            print("The answer is " + answer)  
            speak("The answer is " + answer)  
  
        elif 'search' in query or 'play' in query: 
              
            query = query.replace("search", "")  
            query = query.replace("play", "")           
            webbrowser.open(query)  
  
        elif "who i am" in query:
            print("If you talk then definately your human.")
            speak("If you talk then definately your human.") 
  
        elif "why you came to world" in query: 
            print("Thanks to Ankit. further It's a secret")
            speak("Thanks to Ankit. further It's a secret") 
  
        elif 'is love' in query: 
            print("It is 7th sense that destroy all other senses")
            speak("It is 7th sense that destroy all other senses") 
  
        elif "who are you" in query:
            print("I am your virtual assistant created by Ankit")
            speak("I am your virtual assistant created by Ankit") 
  
        elif 'reason for you' in query:
            print("I was created as a Minor project by Mister Ankit ")
            speak("I was created as a Minor project by Mister Ankit ") 
  
        elif 'open bluestack' in query: 

            try:
                appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
                os.startfile(appli)
            except:
                speak("It is not in your system sir.")
  
        elif 'news' in query: 
              
            try:  
                jsonObj = urlopen('''http://newsapi.org/v2/top-headlines?country=in&apiKey=0decb8ce4f924a43a0fc0150ed065fce''') 
                data = json.load(jsonObj) 
                i = 1                  
                speak('here are some top news from the times of india') 
                print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e)) 
  
          
        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a) 
  
        elif "where is" in query: 
            query = query.replace("where is", "") 
            center = query 
            speak("User asked to Locate") 
            speak(center) 
            webbrowser.open("https://www.google.com/maps/place/" + center + "")
            speak("done")
  
        elif "camera" in query or "take a photo" in query: 
            ec.capture(0, "Jarvis Camera ", "img.jpg") 
  
        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"]) 
  
        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('jarvis.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm:
                now = datetime.now()
                strTime= now.strftime("%H:%M:%S")
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note)
                speak("done sir..")
            else: 
                file.write(note)
                speak("done sir")
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("jarvis.txt", "r")  
            print(file.read()) 
            speak(file.read(6)) 
                 
        # NPPR9-FWDCX-D2C8J-H872K-2YT43 
        elif "jarvis" in query: 
              
            wishMe() 
            speak("Jarvis 1 point o in your service Mister") 
            speak(assname) 
  
        elif "weather" in query:
          driver = webdriver.Chrome()
          speak("Please specify name of the city about which you want to have weather report on the console itself.")
          city = str(input("Enter the name of the city you want the weather forecast for: ")).replace(" ","-")
          try:
              driver.get("https://www.weather-forecast.com/locations/"+city+"/forecasts/latest")
              print(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
              speak(driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text)
          except:
              print("Something went wrong")
          print("The task has been done sir anything else you wish to say")
          speak("The task has been done sir anything else you wish to say")
                      
              
        elif "wikipedia" in query: 
            speak('Searching wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences =2)
            print(results)
            speak(results)
            
  
        elif "good morning" in query: 
            speak("A warm" +query) 
            speak("How are you Mister") 
            speak(assname)

        elif "coronavirus" or "covid-19" in query: 
            while(True):
                  notifyMe("Ankit","Lets stop the corona together .....notifications ahead")
                  myHtmlData = getData('https://www.mohfw.gov.in/')
                  
                  soup = soup = BeautifulSoup(myHtmlData, 'html.parser')
                  print(soup.prettify())
                  myDataStr = ""
                  for tr in soup.find_all('tbody')[0].find_all('tr'):
                       print(tr.get_text())
                       myDataStr += tr.get_text()


                  myDataStr = myDataStr[1:]
                  itemList = myDataStr.split("\n\n")
                  print(itemList)

                  states = ['Chandigarh','Telangana','Uttar Pradesh','Delhi','Bihar','Gujrat']
                  for item in itemList[0:35]:
                    dataList = item.split('\n')
                    print(dataList)
                    #break
                    if dataList[1] in states:
                      #print(dataList)
                      Title = "Cases of Covid-19"
                      Text = f"State {dataList[1]}\nIndian : {dataList[2]} & Foreign : {dataList[3]}\nCured : {dataList[4]}\nDeaths : {dataList[5]} "
                      notifyMe(Title,Text)
                      time.sleep(2)
                  print('Do you want to continue receiving details of corona virus at interval of 1 hour')
                  check = int(input(' press 1 for yes else 0 for no'))
                  if(check==1):
                    time.sleep(3600)
                  else:
                    break
  
  
  
        # most asked question from google Assistant 
        elif "will you be my gf" in query or "will you be my bf" in query:    
            speak("I'm not sure about, may be you should give me some time") 
  
        elif "how are you" in query: 
            speak("I'm fine, glad you me that") 
  
        elif "i love you" in query: 
            speak("It's hard to understand") 
  
       
