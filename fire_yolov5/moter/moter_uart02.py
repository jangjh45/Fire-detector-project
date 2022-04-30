import time
import serial
import pymysql

ser = serial.Serial(port = '/dev/ttyAMA0',
                    baudrate = 9600,
                    timeout = 1)

while True:
    db = pymysql.connect(host='20.194.30.39',
                         user='fire',
                         password='0000',
                         charset='utf8',
                         db='fire_detect')

    cursor = db.cursor()
    sql = "SELECT * FROM detect ORDER BY detect_time DESC limit 1;"
    cursor.execute(sql)
    result = cursor.fetchall()
    for record in result:
        print(record)
    cursor.close()
    time.sleep(1)