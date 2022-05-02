import time
import pymysql
import serial

stop = 5
commend = ['q', 'w', 'e', 'r', 't']
commendnum = None

ser = serial.Serial(port = '/dev/ttyAMA0',
                    baudrate = 9600,
                    timeout = 1)

sql = "SELECT * FROM detect ORDER BY detect_time DESC limit 1;"

while True:
    db = pymysql.connect(host='20.194.30.39',
                         user='fire',
                         password='0000',
                         charset='utf8',
                         db='fire_detect')
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for record in result:
        print(record[0])
        print(record[1])
    db.close()

    if record[1] == 0:
        ser.write('e'.encode('utf-8'))
        commendnum = 2
        if record[1] != 0:
            break
        time.sleep(stop)

        ser.write('w'.encode('utf-8'))
        commendnum = 1
        if record[1] != 0:
            break
        time.sleep(stop)

        ser.write('q'.encode('utf-8'))
        commendnum = 0
        if record[1] != 0:
            break
        time.sleep(stop)

        ser.write('w'.encode('utf-8'))
        commendnum = 1
        if record[1] != 0:
            break
        time.sleep(stop)

        ser.write('e'.encode('utf-8'))
        commendnum = 2
        if record[1] != 0:
            break
        time.sleep(stop)

        ser.write('r'.encode('utf-8'))
        commendnum = 3
        if record[1] != 0:
            break
        time.sleep(stop)

        ser.write('t'.encode('utf-8'))
        commendnum = 4
        if record[1] != 0:
            break
        time.sleep(stop)

        ser.write('r'.encode('utf-8'))
        commendnum = 3
        if record[1] != 0:
            break
        time.sleep(stop)

    elif record[1] == 0:
        ser.write(commend[commendnum].encode('utf-8'))
    else:
        continue