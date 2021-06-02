"""
import pygame
from pygame.version import PygameVersion
"""

"""from tkinter import*
from tkinter.ttk import*
"""

from json import load
import json
import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
from datetime import date
import os
import webbrowser as wb
import requests
#from playsound import playsound
"""
root = Tk()
root.title("Maid al jp")
root.geometry('400x600')
root.iconbitmap('icon.ico')
load=Image.open('icon.png')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0,y=0)
pos_x = 5
pos_y = 35
"""
def speak(audio):
     print("はるか:"+ audio)
     maid.say(audio)
     maid.runAndWait()
"""def screen(audio):
     text=Label(root,text=audio,foreground="#db5196",border=0,background="")
     text.config(font=(('BIZ-UDGothicB',13)))
     text.pack(pady=10)
     #text.after(5000,screen)
"""
def time():
     time=datetime.datetime.now().strftime("%I:%M:%p")
     speak(time)
     print(time)
def welcome():
     hour = datetime.datetime.now().hour
     if hour >= 6 and hour < 12:
        speak("ご機嫌よう、ご主人様。")
     elif hour >= 12 and hour < 18:
        speak("こんにちわんこ、ご主人様。")
     elif hour >= 18 and hour < 24:
        speak("こんばんは、ご主人様。")
     else:
        speak("おやすみなさい、ご主人様")
     speak("あたしをお呼び出しになって誠にありがとうございます、ご主人様。")
     speak("何かご命令なさいますか。ご主人様。")

def meirei():
     m=sr.Recognizer()
     with sr.Microphone() as source:
        m.pause_threshold = 5
        audio = m.listen(source)
     try :
        query=m.recognize_google(audio,language="ja")
        print("ご主人様: "+ query)
     except sr.UnknownValueError :
        """
        maid.say("もう一度キーボードでご命令ください")
        print("もう一度キーボードでご命令ください!")
        screen("もう一度キーボードでご命令ください!")
        box=Text(root,width=28,height=13,font=(('BIZ-UDGothicB',13)))
        box.pack(pady=5)
        query=box.get(1.0,END)
        print(query)
        """
        speak("もう一度キーボードでご命令ください!")
        query=str(input('ご主人様のご命令は:'))
     return query
def meireimusic():
     mm=sr.Recognizer()
     with sr.Microphone() as source:
        mm.pause_threshold = 5
        audio = mm.listen(source)
        mquery=mm.recognize_google(audio,language="ja")
        print("ご主人様: "+ query)
     return mquery
os.system('chcp 10001')
maid=pyttsx3.init()
voices=maid.getProperty('voices')
maid.setProperty('voice',voices[2].id)
newVoiceRate = 130
maid.setProperty('rate',newVoiceRate)
maid.say("あたしははるかでございます。")
print("はるか:あたしははるかでございます。")
maid.runAndWait()
if __name__ == "__main__":
        welcome()
        while True:
            query=meirei().lower()
            if "google" in query:
             speak('何をご検索なさいますか。')
             search=meirei().lower()
             url=f"https://www.google.com/search?q={search}"
             wb.get().open(url)
             speak(f"こちらは検索いたした{search}でございます。")
            elif "youtube" in query:
             speak('何をご検索なさいますか。')
             search=meirei().lower()
             url=f"https://www.youtube.com/search?q={search}"
             wb.get().open(url)
             speak(f"こちらは検索いたした{search}でございます。")
            elif "時間" in query:
             time()
            elif "ゲーム" in query:
             speak('ご主人様のおゲームは:')
             game=str(input(r'ご主人様のおゲームのファイルパスは:'))
             speak('ゲームをスタートいたしています。')
             os.startfile(game)
            elif "音楽" in query:
             speak("数字でご音楽のタイプを選びください、1はファイルで、2はインターネットで:")
             try:
              speak("ご主人様の声で。")
              music_type=meireimusic().lower()
             except sr.UnknownValueError :
              speak("キーボードでご命令ください。")
              music_type = int(input('1.ファイルで、2.インターネットで:'))
             if music_type == 1 or '一' in music_type or '1' in music_type:
              speak('ご主人様のお曲のファイルパスは:') 
              music1=str(input(r'ご主人様のお曲のファイルパスは:'))
              try:
               os.startfile(music1)
               speak("音楽をスタートいたしています。")
              except:
               speak('本当にすみません、ファイルパスが見つけられませんでした。')
             if music_type == 2 or '二' in music_type or '2' in music_type:
               speak('ご主人様のお曲の名前は:')
               music2 = str(input('ご主人様のお曲の名前は:'))
               murl = f'https://zingmp3.vn/tim-kiem/bai-hat?q={music2}'
               wb.get().open(murl)
               speak("音楽をスタートいたしています。")
            elif "コロナ" in query:
               print("COVID NEWS:　")
               url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"
               querystring = {"country":"vietnam"}
               headers = {
               'x-rapidapi-key': "9a129215dfmshe7cd1ce634fd89cp12265bjsn14fec4b1385a",
               'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com"
              }
               response = requests.request("GET", url, headers=headers, params=querystring)
               data = response.json()
               texts = data["latest_stat_by_country"]
               for text in texts:
                  print("Country: "+text["country_name"])
                  print("Total cases: "+text["total_cases"])
                  print("New　cases: "+text["new_cases"])
                  print("Active　cases: "+text["active_cases"])
                  print("Total　deaths: "+text["total_deaths"])
                  print("New　deaths: "+text["new_deaths"])
                  print("Total　recovered: "+text["total_recovered"])
                  print("Record　date: "+text["record_date"])
            elif "辞書" in query:
               import googletrans
               from googletrans import Translator
               speak('日本語の言葉を入力ください:')
               t = Translator()
               input_text = str(input('日本語の言葉を入力ください:'))
               a = t.translate(input_text,src="ja",dest="vi")
               print("ベトナムの言葉:"+a.text)
            elif  "アニメ" in query:
               print("TOP AIRING ANIME:")
               url = "https://jikan1.p.rapidapi.com/top/anime/1/airing"
               headers = {
                 'x-rapidapi-key': "9a129215dfmshe7cd1ce634fd89cp12265bjsn14fec4b1385a",
                 'x-rapidapi-host': "jikan1.p.rapidapi.com"
                }
               response = requests.request("GET", url, headers=headers)
               data = response.json()
               texts = data["top"]
               for text in texts :
                  print(f'Rank: {text["rank"]}')
                  print(f'Title: {text["title"]}')
                  print(f'Score: {text["score"]}')
                  print(f'Type: {text["type"]}')
                  print(f'Episodes: {text["episodes"]}')
                  print("============================")
            elif "漫画" in query:
               print("TOP MANGA: ")
               url = "https://jikan1.p.rapidapi.com/top/manga/1/manga"
               headers = {
                    'x-rapidapi-key': "9a129215dfmshe7cd1ce634fd89cp12265bjsn14fec4b1385a",
                    'x-rapidapi-host': "jikan1.p.rapidapi.com"
                }
               response = requests.request("GET", url, headers=headers)
               data = response.json()
               #print(json.dumps(data,indent=2))
               texts = data["top"]
               for text in texts :
                  print(f'Rank: {text["rank"]}')
                  print(f'Title: {text["title"]}')
                  print(f'Score: {text["score"]}')
                  print(f'Type: {text["type"]}')
                  print(f'Volumes: {text["volumes"]}')
                  print("============================")
            elif "サッカー" in query:
               print("SOCCER TODAY: ")
               url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
               querystring = {"date":date.today().strftime("%Y-%m-%d")}
               headers = {
                 'x-rapidapi-key': "9a129215dfmshe7cd1ce634fd89cp12265bjsn14fec4b1385a",
                 'x-rapidapi-host': "api-football-v1.p.rapidapi.com"
                }
               response = requests.request("GET", url, headers=headers, params=querystring)
               data = json.loads(response.text)
               # print(json.dumps(data,indent=2))
               # texts = data['response']['fixture']
               texts = data["response"]
               #texts2 = texts[0]["fixture"]
               for text in texts:
                  print(f'{text["league"]["country"]} - {text["league"]["name"]}:')
                  print(f'{text["teams"]["home"]["name"]}  {text["goals"]["home"]}')
                  print(f'     min: {text["fixture"]["status"]["elapsed"]}')
                  print(f'{text["teams"]["away"]["name"]}  {text["goals"]["away"]}')
                  print("=====================")
            elif "野球" in query:
               speak("数字でリーグを選びください、ご主人様。一はアメリカリーグ、二は日本リーグ。")
               try:
                  speak('ご主人様の声で。')
                  league=meireimusic().lower()
               except sr.UnknownValueError :
                  speak("キーボードでご命令ください。")
                  league = int(input('1.アメリカリーグ、2.日本リーグ:'))
               if league == 1 or '一' in league or '1' in league:
                  print("MAJOR LEAGUE BASEBALL: ")
                  url = "https://api-baseball.p.rapidapi.com/games"
                  querystring = {"league":"1","season":"2021","date":date.today().strftime("%Y-%m-%d")}
                  headers = {
                  'x-rapidapi-key': "9a129215dfmshe7cd1ce634fd89cp12265bjsn14fec4b1385a",
                  'x-rapidapi-host': "api-baseball.p.rapidapi.com"
                 }
                  response = requests.request("GET", url, headers=headers, params=querystring)
                  data = response.json()
                  texts = data["response"]
                  for text in texts :
                    print(f'{text["country"]["name"]} - {text["league"]["name"]}')
                    print(f'{text["status"]["long"]}')
                    print(f'{text["teams"]["home"]["name"]}: {text["scores"]["home"]["innings"]["1"]} {text["scores"]["home"]["innings"]["2"]} {text["scores"]["home"]["innings"]["3"]} {text["scores"]["home"]["innings"]["4"]} {text["scores"]["home"]["innings"]["5"]} {text["scores"]["home"]["innings"]["6"]} {text["scores"]["home"]["innings"]["7"]} {text["scores"]["home"]["innings"]["8"]} {text["scores"]["home"]["innings"]["9"]} Extra innings:{text["scores"]["home"]["innings"]["extra"]} | R:{text["scores"]["home"]["total"]} H:{text["scores"]["home"]["hits"]} E:{text["scores"]["home"]["errors"]}')
                    print(f'{text["teams"]["away"]["name"]}: {text["scores"]["away"]["innings"]["1"]} {text["scores"]["away"]["innings"]["2"]} {text["scores"]["away"]["innings"]["3"]} {text["scores"]["away"]["innings"]["4"]} {text["scores"]["away"]["innings"]["5"]} {text["scores"]["away"]["innings"]["6"]} {text["scores"]["away"]["innings"]["7"]} {text["scores"]["away"]["innings"]["8"]} {text["scores"]["away"]["innings"]["9"]} Extra innings:{text["scores"]["away"]["innings"]["extra"]} | R:{text["scores"]["away"]["total"]} H:{text["scores"]["away"]["hits"]} E:{text["scores"]["away"]["errors"]}')                   
                    print("=================================================================================================")
               if league == 2 or '二' in league or '2' in league:
                  print("NIPPON PROFESSIONAL BASEBALL: ")
                  url = "https://api-baseball.p.rapidapi.com/games"
                  querystring = {"league":"2","season":"2021","date":date.today().strftime("%Y-%m-%d")}
                  headers = {
                  'x-rapidapi-key': "9a129215dfmshe7cd1ce634fd89cp12265bjsn14fec4b1385a",
                  'x-rapidapi-host': "api-baseball.p.rapidapi.com"
                 }
                  response = requests.request("GET", url, headers=headers, params=querystring)
                  data = response.json()
                  texts = data["response"]
                  for text in texts :
                    print(f'{text["country"]["name"]} - {text["league"]["name"]}')
                    print(f'{text["status"]["long"]}')
                    print(f'{text["teams"]["home"]["name"]}: {text["scores"]["home"]["innings"]["1"]} {text["scores"]["home"]["innings"]["2"]} {text["scores"]["home"]["innings"]["3"]} {text["scores"]["home"]["innings"]["4"]} {text["scores"]["home"]["innings"]["5"]} {text["scores"]["home"]["innings"]["6"]} {text["scores"]["home"]["innings"]["7"]} {text["scores"]["home"]["innings"]["8"]} {text["scores"]["home"]["innings"]["9"]} Extra innings:{text["scores"]["home"]["innings"]["extra"]} | R:{text["scores"]["home"]["total"]} H:{text["scores"]["home"]["hits"]} E:{text["scores"]["home"]["errors"]}')
                    print(f'{text["teams"]["away"]["name"]}: {text["scores"]["away"]["innings"]["1"]} {text["scores"]["away"]["innings"]["2"]} {text["scores"]["away"]["innings"]["3"]} {text["scores"]["away"]["innings"]["4"]} {text["scores"]["away"]["innings"]["5"]} {text["scores"]["away"]["innings"]["6"]} {text["scores"]["away"]["innings"]["7"]} {text["scores"]["away"]["innings"]["8"]} {text["scores"]["away"]["innings"]["9"]} Extra innings:{text["scores"]["away"]["innings"]["extra"]} | R:{text["scores"]["away"]["total"]} H:{text["scores"]["away"]["hits"]} E:{text["scores"]["away"]["errors"]}')                   
                    print("=================================================================================================")
               #print(json.dumps(data,indent=2))
            elif "天気" in query :
               url = "https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"
               querystring = {"apikey":"873dbe322aea47f89dcf729dcc8f60e8"}
               headers = {
                 'x-rapidapi-key': "9a129215dfmshe7cd1ce634fd89cp12265bjsn14fec4b1385a",
                 'x-rapidapi-host': "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com"
                } 
               response1 = requests.request("GET", url, headers=headers, params=querystring)
               data1 = response1.json()
               text1 = data1["ip"]
               print(f'Your IP: {text1}')
               url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
               querystring = {"q":f'{text1}',"days":"1"}
               headers = {
                'x-rapidapi-key': "9a129215dfmshe7cd1ce634fd89cp12265bjsn14fec4b1385a",
                'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
               }
               response2 = requests.request("GET", url, headers=headers, params=querystring)
               data2 = response2.json()
               print("CURRENT WEATHER IN YOUR LOCATION DEFINED BY YOUR IP:")
               print(f'Location: {data2["location"]["name"]}')
               print(f'Country: {data2["location"]["country"]}')
               print(f'Temperature: {data2["current"]["temp_c"]}C')
               print(f'Condition: {data2["current"]["condition"]["text"]}')
               print(f'Humidity: {data2["current"]["humidity"]}%')
            elif "アウト" in query:
             speak("またこの度お目にかかります、ご主人様。")
             quit()
            else:
               speak('本当にすみませんでした、あたしはご主人様のご命令を実行できませんでした。')
            speak("ご命令を続けください、ご主人様。")
input()











    




