import time
import serial
import pymysql

# 전역변수 선언부 
db = None 
cur = None
stop_time = 5
loc0 = 'q'
loc45 = 'w'
loc90 = 'e'
loc135 = 'r'
loc180 = 't'

point1 = 'pin1'
point2 = 'pin2'
point3 = 'pin3'
point4 = 'pin4'
point5 = 'pin5'

ser = serial.Serial(port = '/dev/ttyAMA0',
                    baudrate = 9600,
                    timeout = 1)

ser.write(loc90.encode('utf-8'))

conn = pymysql.connect(host='20.194.30.39',
                       user='fire',
                       password='0000',
                       charset='utf8',
                       db='fire_detect') #DB 연결
                        
cur = conn.cursor() #디폴트 커서 생성



while True:
    ser.write(loc0.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point1))
    conn.commit()
    time.sleep(stop_time)

    ser.write(loc30.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point2))
    conn.commit()
    time.sleep(stop_time)

    ser.write(loc60.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point3))
    conn.commit()
    time.sleep(stop_time)
    
    ser.write(loc90.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point4))
    conn.commit()
    time.sleep(stop_time)

    ser.write(loc120.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point5))
    conn.commit()
    time.sleep(stop_time)

    ser.write(loc150.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point6))
    conn.commit()
    time.sleep(stop_time)

    ser.write(loc180.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point7))
    conn.commit()
    time.sleep(stop_time)

    ser.write(loc150.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point6))
    conn.commit()
    time.sleep(stop_time)

    ser.write(loc120.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point5))
    conn.commit()
    time.sleep(stop_time)

    ser.write(loc90.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point4))
    conn.commit()
    time.sleep(stop_time)

    ser.write(loc60.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point3))
    conn.commit()
    time.sleep(stop_time)

    ser.write(loc30.encode('utf-8'))
    sql = "INSERT INTO location (time, location) VALUES (NOW(), %s);"
    cur.execute(sql, (point2))
    conn.commit()
    time.sleep(stop_time)