import time
import pymysql
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin=18

# 전역변수 선언부 
db = None 
cur = None

conn = pymysql.connect(host='20.194.30.39',
                       user='fire',
                       password='0000',
                       charset='utf8',
                       db='fire_detect') #DB 연결
                        
cur = conn.cursor() #디폴트 커서 생성

def temper():
    global db, cur, conn

    while(True):
        h, t = Adafruit_DHT.read_retry(sensor, pin)
        if (h is not None) and (t is not None) :
            tem = ("{:.1f}".format(t))
            hum = ("{:.1f}".format(h))
            sql = "INSERT INTO temper (time, temperature, humidity) VALUES (NOW(), %s, %s);"
            cur.execute(sql, (tem, hum))
            print(tem)
            print(hum)
        else:
            continue

        conn.commit()
        print('rowcount: ', cur.rowcount)
        time.sleep(2)
    
if __name__== "__main__":
    temper()