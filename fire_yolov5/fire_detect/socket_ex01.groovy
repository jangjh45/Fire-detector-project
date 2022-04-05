import socket 
import os
import RPi.GPIO as GPIO 
import time
from youtubesearchpython import * #pip install youtube-search-python
import yapi
from datetime import datetime
import webbrowser
from selenium import webdriver

from _thread import *

import mysql.connector
mydb = mysql.connector.connect(
    host="DB ADDRESS",
    port = PORT,
    user="ID",
    passwd="PASSWORD",
    database="detect_server" 
)
mc = mydb.cursor()

relay_1 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_1, GPIO.OUT)
GPIO.output(relay_1, GPIO.LOW)

sql = "UPDATE speech SET playing = %s, playing_title = %s WHERE id = 1"
val = ('NO', 'NONE')
mc.execute(sql, val)
mydb.commit()

def speak(msg, option) :
    os.system("gtts-cli '" + msg + "' " + option)

def speech_reset():
    sql = "UPDATE speech SET speech_detect = %s WHERE id = 1"
    val = ('checked', )
    mc.execute(sql, val)
    mydb.commit()
    time.sleep(2.5)
    sql = "UPDATE speech SET speech_detect = %s WHERE id = 1"
    val = ('NONE', )
    mc.execute(sql, val)
    mydb.commit()

def threaded(client_socket, addr): 

    print('클라이언트가 접속되었습니다. 접속정보 :', addr[0], ':', addr[1]) 

    while True: 

        try:

            data = client_socket.recv(1024)

            if not data: 
                print('클라이언트 연결 끊어짐 : ' + addr[0],':',addr[1])
                break

            sql = "SELECT * FROM weather_info"
            mc.execute(sql)
            sqldata = mc.fetchall()
            mydb.commit()

            current = sqldata[0][1]
            weather_info = sqldata[0][2]
            today_info = sqldata[0][3]

            if(weather_info == '맑음'):
                weather_info = '맑을'
            elif(weather_info == '흐림'):
                weather_info = '흐릴'
            elif(weather_info == '눈'):
                weather_info = '눈이 올'
            elif(weather_info == '비'):
                weather_info = '비가 올'
            elif(weather_info == '구름많음'):
                weather_info = '구름이 많을'
            
            

            option = '--lang ko | mpg123 -'
            target = data.decode()#.replace('| Detect!','')

            if '음성인식 :' in target:
                target = target.replace("백호야", "에코야").replace("백호 야", "에코 야")
                print('다음 음성이 인식됨 : ' + target.replace('음성인식 : ',''))
                if '날씨알려줘' in target:
                    speak('오늘은 ' + weather_info + '예정 이며, 기온은 ' + current + '° 입니다. ' + today_info,option)
                    speech_reset()
                elif '안녕' in target:
                    speak('안녕하세요. 반가워요.',option)
                    speech_reset()
                elif '모니터 켜' in target:
                    GPIO.output(relay_1, GPIO.HIGH)
                    speak('네 모니터를 켤게요',option)
                elif '모니터 꺼' in target:
                    GPIO.output(relay_1, GPIO.LOW)
                    speak('네 모니터를 끌게요',option)
                elif '+' in target:
                    num1 = target.split(" + ")[0].replace("음성인식 :", "").replace("은", "").replace("는", "").replace(",", "")
                    num2 = target.split(" + ")[1].replace("음성인식 :", "").replace("은", "").replace("는", "").replace(",", "")
                    sum = int(num1) + int(num2)
                    sum = str(sum)
                    #sum.replace("음성인식 :", "").replace("은", "").replace("는", "")
                    speak(num1 + ' 더하기 ' + num2 + '은 ' + sum + '입니다.',option)
                    speech_reset()
                elif '코로나' in target:

                    today = str(datetime.today()).split(" ")[0]

                    sql = "SELECT * FROM corona_info WHERE date = %s"
                    val = (today, )
                    mc.execute(sql, val)
                    data = mc.fetchall()
                    mydb.commit()
                    if not data:
                        sql_today_data = "NO"
                        speak('오늘 코로나 확진자가 아직 집계되지 않았어요. 스마트 미러를 실행하여 집계를 완료해주세요.',option)
                        speech_reset()
                    else:
                        today_corona = data[0][2]
                        sql = "SELECT * FROM corona_info ORDER BY date DESC LIMIT 2;"
                        #val = (today, )
                        mc.execute(sql)
                        data = mc.fetchall()
                        mydb.commit()

                        yesterday_confirmation = data[1][2].replace(',', '')
                        today_confirmation = data[0][2].replace(',', '')
                        cel_confirmation = int(today_confirmation) - int(yesterday_confirmation)
                        cel_confirmation = str(cel_confirmation)
                        if cel_confirmation == '0':
                            cel_confirmation = cel_confirmation.replace('-','')
                            speak('오늘 코로나 확진자는 ' + today_corona + '명 이에요.',option)
                            speech_reset()
                        elif '-' in cel_confirmation:
                            cel_confirmation = cel_confirmation.replace('-','')
                            speak('오늘 코로나 확진자는 ' + today_corona + '명 이에요. 어제보다 ' + cel_confirmation + '명 적어요.',option)
                            speech_reset()
                        else:
                            #cel_confirmation = cel_confirmation.replace('-','')
                            speak('오늘 코로나 확진자는 ' + today_corona + '명 이에요. 어제보다 ' + cel_confirmation + '명 많아요.',option)
                            speech_reset()
                elif '최근 감지' in target:
                    sql = "SELECT * FROM maindb ORDER BY in_time DESC LIMIT 1 "
                    mc.execute(sql)
                    sqldata = mc.fetchall()
                    mydb.commit()

                    username = sqldata[0][1]
                    if(username == 'SeungHwan'):
                        username = '승환'
                    # = sqldata[0][2]
                    #today_info = sqldata[0][3]
                    speak('최근 감지된 사람은 ' + username + '님 이에요.',option)
                    speech_reset()
                elif '기온' in target:
                    speak('현재 기온은 ' + current + '° 입니다.',option)
                    speech_reset()
                elif '누구' in target:
                    speak('저는 에코 입니다. GOOGLE ASSISTANT 기반으로 만들어졌어요.',option)
                    speech_reset()
                elif '음악 종료' in target:
                    sql = "SELECT * FROM speech"
                    mc.execute(sql)
                    sqldata = mc.fetchall()
                    mydb.commit()

                    playing = sqldata[0][1]
                    if(playing == 'NO'):
                        speak('지금 재생 중인 곡이 없어요.',option)
                        speech_reset()
                    elif(playing == 'YES'):
                        driver.quit()
                        speak('네 음악 재생을 종료 할게요.',option)
                        sql = "UPDATE speech SET playing = %s, playing_title = %s WHERE id = 1"
                        val = ('NO', 'NONE')
                        mc.execute(sql, val)
                        mydb.commit()
                        speech_reset()
                elif '재생 중인 음악' in target:
                    sql = "SELECT * FROM speech"
                    mc.execute(sql)
                    sqldata = mc.fetchall()
                    mydb.commit()

                    playing = sqldata[0][1]
                    playing_title = sqldata[0][2]
                    if(playing == 'NO'):
                        speak('지금 재생 중인 곡이 없어요.',option)
                        speech_reset()
                    elif(playing == 'YES'):
                        speak('지금 재생 중인 음악은 ' + playing_title + ' 이에요.',option)
                        speech_reset()
                elif '틀어 줘' in target:
                    sql = "SELECT * FROM speech"
                    mc.execute(sql)
                    sqldata = mc.fetchall()
                    mydb.commit()

                    playing = sqldata[0][1]

                    
                    if '에코야' in target:
                        video_name = target.split('에코야 ')[1].split('틀어 줘')[0]
                    elif '에코 야' in target:
                        video_name = target.split('에코 야 ')[1].split('틀어 줘')[0]

                    video_name = video_name.replace("에코야", "").replace("에코 야", "").replace("   ", "").replace("  ", "")
                    if not video_name:
                        speak('죄송하지만, 제목을 다시 말씀해주세요.',option)
                        speech_reset()
                    else:
                        if(playing == 'NO'):
                            print(video_name)
                            speak('네 유튜브에서 ' + video_name + '을 들려 드릴게요',option)
                            speech_reset()
                            api = yapi.YoutubeAPI('AIzaSyAR1nbBHbuNhYy61v7F6PuVaow_1ak57I0')
                            results = api.general_search(video_name, max_results=2)
                            str_results=str(results)

                            video_id = str_results.split(', videoId=\'')[1].split('\'),')[0]

                            videoFormats = str(Video.getFormats(video_id))

                            #print(videoFormats)
                            url = videoFormats.split('url\': \'')[1].split('\'')[0]
                            #print(url)
                            driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
                            driver.get(url)
                            driver.minimize_window()
                            #driver.maximize_window()

                            sql = "UPDATE speech SET playing = %s, playing_title = %s WHERE id = 1"
                            val = ('YES', video_name)
                            mc.execute(sql, val)
                            mydb.commit()
                        elif(playing == 'YES'):
                            driver.quit()
                            speak('네 지금 재생중인 곡을 멈추고, ' + video_name + '을 들려 드릴게요',option)
                            speech_reset()
                            api = yapi.YoutubeAPI('AIzaSyAR1nbBHbuNhYy61v7F6PuVaow_1ak57I0')
                            results = api.general_search(video_name, max_results=2)
                            str_results=str(results)

                            video_id = str_results.split(', videoId=\'')[1].split('\'),')[0]

                            videoFormats = str(Video.getFormats(video_id))

                            #print(videoFormats)
                            url = videoFormats.split('url\': \'')[1].split('\'')[0]
                            #print(url)
                            driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
                            driver.get(url)
                            driver.minimize_window()
                            #driver.maximize_window()
                            sql = "UPDATE speech SET playing = %s, playing_title = %s WHERE id = 1"
                            val = ('YES', video_name)
                            mc.execute(sql, val)
                            mydb.commit()
                        #webbrowser.open(url)
                else:
                    speech_reset()

                

                    
            else:
                if target == "SeungHwan":
                    speak('승환 님 안녕하세요 반가워요. 오늘은 ' + weather_info + '예정 이며, ' + today_info,option)

                elif target == "HyeonWoo":
                    speak('현우 님 안녕하세요 반가워요. 오늘은 ' + weather_info + '예정 이며, ' + today_info,option)

                elif target == "Siro":
                    speak('시로 님 안녕하세요 반가워요. 오늘은 ' + weather_info + '예정 이며, ' + today_info,option)

                elif target == "HyeongCheon":
                    speak('형천 님 안녕하세요 반가워요. 오늘은 ' + weather_info + '예정 이며, ' + today_info,option)
                    print(target)

                else:
                    msg = 'Warning! 인증되지 않은 사용자가 감지 되었습니다.'
                    speak(msg,option)


                print('Received from ' + addr[0],':',addr[1] , data.decode())
                if target == 'SeungHwan':
                    GPIO.output(relay_1, GPIO.HIGH)
            

            client_socket.send(data) 

        except ConnectionResetError as e:

            print('클라이언트 연결 끊어짐 : ' + addr[0],':',addr[1])
            break
             
    client_socket.close() 

HOST = '0.0.0.0'
PORT = 13388

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT)) 
server_socket.listen() 

print('소켓 서버 시작중...')

try:

    while True: 

        print('클라이언트 접속 대기...')


        client_socket, addr = server_socket.accept() 
        start_new_thread(threaded, (client_socket, addr))
        
    server_socket.close()

        
except KeyboardInterrupt:
    GPIO.cleanup()
    sql = "UPDATE speech SET playing = %s, playing_title = %s WHERE id = 1"
    val = ('NO', 'NONE')
    mc.execute(sql, val)
    mydb.commit()