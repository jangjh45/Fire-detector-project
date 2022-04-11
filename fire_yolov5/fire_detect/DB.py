import os
import glob
import time
import pymysql

# 전역변수 선언부 
db = None 
cur = None

conn = pymysql.connect(host='192.168.1.202', user='root', password='1234', charset='utf8', db='detect') #DB 연결
cur = conn.cursor() #디폴트 커서 생성

dir_PATH = 'C:/yolov5-master/runs'
labels_PATH = 'C:/yolov5-master/runs/detect/exp/labels'
txt_PATH = 'C:/yolov5-master/runs/detect/exp/labels/*.txt'

fire_count = 0
non_fire_count = 0

while(True):
    # secs = time.time()
    # tm = time.localtime(secs)
    # string = time.strftime('%Y-%m-%d %I:%M:%S', tm)
    # print(string)

    dir_list = os.listdir(dir_PATH)
    dir_count = len(dir_list)
    #print(dir_count)
    if dir_count == 0: #폴더가 없으면 아래 코드 무시 1개이상 있으면 아래 코드 실행
        continue
    
    file_list = os.listdir(labels_PATH)
    file_count = len(file_list)
    #print(file_count)
    if file_count == 0: #폴더안에 좌표값txt가 없으면 아래 코드 무시 1개이상 있으면 아래 코드 실행
        continue
    
    label_list = sorted(glob.glob(txt_PATH), key=os.path.getctime, reverse=True)
    first_list = label_list[0]
    time.sleep(2)
    label_list2 = sorted(glob.glob(txt_PATH), key=os.path.getctime, reverse=True)
    second_list = label_list2[0]     
    print(first_list)
    print(second_list)
    
    if first_list != second_list:   
        fire_count += 1 
        non_fire_count = 0
        print(fire_count)
        print(non_fire_count)
        print('\n')
    else: 
        fire_count == second_list
        non_fire_count += 1
        fire_count = 0
        print(fire_count)
        print(non_fire_count)
        print('\n')
    
    if fire_count >= 3 and non_fire_count == 0:
        sql = "INSERT INTO detect_table (state, TIME) VALUES ('fire', NOW());"
        print("화재 발생!!")
    elif fire_count < 3 and non_fire_count < 3:
        sql = "INSERT INTO detect_table (state, time) VALUES ('loading', NOW());"
        print("상황파악중") 
    else:
        non_fire_count >= 3 and fire_count == 0
        sql = "INSERT INTO detect_table (state, time) VALUES ('non_fire', NOW());"
        print("화재 상황 종료")
    cur.execute(sql)
    conn.commit()
    print('rowcount: ', cur.rowcount)
