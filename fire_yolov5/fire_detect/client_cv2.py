import os
import cv2
import numpy as np
import glob
import time
from rmfile import *


rtsp_PATH = 'http://192.168.0.11:50036/?action=stream'
dir_PATH = 'C:/yolov5-master/runs'
labels_PATH = 'C:/yolov5-master/runs/detect/exp/labels'
txt_PATH = 'C:/yolov5-master/runs/detect/exp/labels/*.txt'
cv_text = 'fire'

cap = cv2.VideoCapture(rtsp_PATH)
frame_W = 640
frame_H = 480

while(True):
    dir_list = os.listdir(dir_PATH)
    dir_count = len(dir_list)
    #print(dir_count)
    if dir_count == 0: #폴더가 없으면 아래 코드 무시 1개이상 있으면 아래 코드 실행
        continue
    #time.sleep(0.01)
    file_list = os.listdir(labels_PATH)
    file_count = len(file_list)
    #print(file_count)
    if file_count == 0: #폴더안에 좌표값txt가 없으면 아래 코드 무시 1개이상 있으면 아래 코드 실행
        continue
    #time.sleep(0.01)
    label_list = sorted(glob.glob(txt_PATH), key=os.path.getctime, reverse=True)
    first_list = label_list[0] #label폴더에서 마지막생성 좌표 경로 리스트 저장
    #print(first_list)
    
    with open(first_list) as f:   #txt파일을 읽어 각 행 개수 파악
        txt_len = len(f.readlines())
        #print(txt_len)
        f.close()
    
    with open(first_list) as y: #txt파일을 읽어 각 행 좌표를 리스트에 저장
        if txt_len == 1:
            xywh1 = y.read().splitlines()
            xywh1_1R = xywh1[0]
            # print(xywh1_1R)
            # print(xywh1_1R[6:11])
            # print(xywh1_1R[12:17])
            # print(xywh1_1R[18:23])
            # print(xywh1_1R[24:29])
            # print(float(xywh1_1R[6:11])*frame_H)
            # print(int((float(xywh1_1R[6:11])*frame_W)-((float(xywh1_1R[18:23])/2)*frame_W)))
        elif txt_len == 2:
            xywh2 = y.read().splitlines()
            xywh2_1R = xywh2[0]
            xywh2_2R = xywh2[1]
        elif txt_len == 3:
            xywh3 = y.read().splitlines()
            xywh3_1R = xywh3[0]
            xywh3_2R = xywh3[1]
            xywh3_3R = xywh3[2]
        elif txt_len == 4:
            xywh4 = y.read().splitlines()
            xywh4_1R = xywh4[0]
            xywh4_2R = xywh4[1]
            xywh4_3R = xywh4[2]
            xywh4_4R = xywh4[3]
        elif txt_len == 5:
            xywh5 = y.read().splitlines()
            xywh5_1R = xywh5[0]
            xywh5_2R = xywh5[1]
            xywh5_3R = xywh5[2]
            xywh5_4R = xywh5[3]
            xywh5_5R = xywh5[4]
        else:
            continue
        y.close()
    
    ret, frame = cap.read()
    if txt_len == 1:
        cv2.rectangle(frame, 
        (int((float(xywh1_1R[6:11])*frame_W)-((float(xywh1_1R[18:23])/2)*frame_W)),
        int((float(xywh1_1R[12:17])*frame_H)-((float(xywh1_1R[24:29])/2)*frame_H)),
        int((float(xywh1_1R[18:23]))*frame_W),
        int((float(xywh1_1R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh1_1R[6:11])*frame_W)-((float(xywh1_1R[18:23])/2)*frame_W)),
        int((float(xywh1_1R[12:17])*frame_H)-((float(xywh1_1R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

    elif txt_len == 2:
        cv2.rectangle(frame, 
        (int((float(xywh2_1R[6:11])*frame_W)-((float(xywh2_1R[18:23])/2)*frame_W)),
        int((float(xywh2_1R[12:17])*frame_H)-((float(xywh2_1R[24:29])/2)*frame_H)),
        int((float(xywh2_1R[18:23]))*frame_W),
        int((float(xywh2_1R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh2_1R[6:11])*frame_W)-((float(xywh2_1R[18:23])/2)*frame_W)),
        int((float(xywh2_1R[12:17])*frame_H)-((float(xywh2_1R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

        cv2.rectangle(frame, 
        (int((float(xywh2_2R[6:11])*frame_W)-((float(xywh2_2R[18:23])/2)*frame_W)),
        int((float(xywh2_2R[12:17])*frame_H)-((float(xywh2_2R[24:29])/2)*frame_H)),
        int((float(xywh2_2R[18:23]))*frame_W),
        int((float(xywh2_2R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh2_2R[6:11])*frame_W)-((float(xywh2_2R[18:23])/2)*frame_W)),
        int((float(xywh2_2R[12:17])*frame_H)-((float(xywh2_2R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

    elif txt_len == 3:
        cv2.rectangle(frame, 
        (int((float(xywh3_1R[6:11])*frame_W)-((float(xywh3_1R[18:23])/2)*frame_W)),
        int((float(xywh3_1R[12:17])*frame_H)-((float(xywh3_1R[24:29])/2)*frame_H)),
        int((float(xywh3_1R[18:23]))*frame_W),
        int((float(xywh3_1R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh3_1R[6:11])*frame_W)-((float(xywh3_1R[18:23])/2)*frame_W)),
        int((float(xywh3_1R[12:17])*frame_H)-((float(xywh3_1R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

        cv2.rectangle(frame, 
        (int((float(xywh3_2R[6:11])*frame_W)-((float(xywh3_2R[18:23])/2)*frame_W)),
        int((float(xywh3_2R[12:17])*frame_H)-((float(xywh3_2R[24:29])/2)*frame_H)),
        int((float(xywh3_2R[18:23]))*frame_W),
        int((float(xywh3_2R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh3_2R[6:11])*frame_W)-((float(xywh3_2R[18:23])/2)*frame_W)),
        int((float(xywh3_2R[12:17])*frame_H)-((float(xywh3_2R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

        cv2.rectangle(frame, 
        (int((float(xywh3_3R[6:11])*frame_W)-((float(xywh3_3R[18:23])/2)*frame_W)),
        int((float(xywh3_3R[12:17])*frame_H)-((float(xywh3_3R[24:29])/2)*frame_H)),
        int((float(xywh3_3R[18:23]))*frame_W),
        int((float(xywh3_3R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh3_3R[6:11])*frame_W)-((float(xywh3_3R[18:23])/2)*frame_W)),
        int((float(xywh3_3R[12:17])*frame_H)-((float(xywh3_3R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

    elif txt_len == 4:
        cv2.rectangle(frame, 
        (int((float(xywh4_1R[6:11])*frame_W)-((float(xywh4_1R[18:23])/2)*frame_W)),
        int((float(xywh4_1R[12:17])*frame_H)-((float(xywh4_1R[24:29])/2)*frame_H)),
        int((float(xywh4_1R[18:23]))*frame_W),
        int((float(xywh4_1R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh4_1R[6:11])*frame_W)-((float(xywh4_1R[18:23])/2)*frame_W)),
        int((float(xywh4_1R[12:17])*frame_H)-((float(xywh4_1R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

        cv2.rectangle(frame, 
        (int((float(xywh4_2R[6:11])*frame_W)-((float(xywh4_2R[18:23])/2)*frame_W)),
        int((float(xywh4_2R[12:17])*frame_H)-((float(xywh4_2R[24:29])/2)*frame_H)),
        int((float(xywh4_2R[18:23]))*frame_W),
        int((float(xywh4_2R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh4_2R[6:11])*frame_W)-((float(xywh4_2R[18:23])/2)*frame_W)),
        int((float(xywh4_2R[12:17])*frame_H)-((float(xywh4_2R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

        cv2.rectangle(frame, 
        (int((float(xywh4_3R[6:11])*frame_W)-((float(xywh4_3R[18:23])/2)*frame_W)),
        int((float(xywh4_3R[12:17])*frame_H)-((float(xywh4_3R[24:29])/2)*frame_H)),
        int((float(xywh4_3R[18:23]))*frame_W),
        int((float(xywh4_3R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh4_3R[6:11])*frame_W)-((float(xywh4_3R[18:23])/2)*frame_W)),
        int((float(xywh4_3R[12:17])*frame_H)-((float(xywh4_3R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

        cv2.rectangle(frame, 
        (int((float(xywh4_4R[6:11])*frame_W)-((float(xywh4_4R[18:23])/2)*frame_W)),
        int((float(xywh4_4R[12:17])*frame_H)-((float(xywh4_4R[24:29])/2)*frame_H)),
        int((float(xywh4_4R[18:23]))*frame_W),
        int((float(xywh4_4R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh4_4R[6:11])*frame_W)-((float(xywh4_4R[18:23])/2)*frame_W)),
        int((float(xywh4_4R[12:17])*frame_H)-((float(xywh4_4R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)
    
    elif txt_len == 5:
        cv2.rectangle(frame, 
        (int((float(xywh5_1R[6:11])*frame_W)-((float(xywh5_1R[18:23])/2)*frame_W)),
        int((float(xywh5_1R[12:17])*frame_H)-((float(xywh5_1R[24:29])/2)*frame_H)),
        int((float(xywh5_1R[18:23]))*frame_W),
        int((float(xywh5_1R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh5_1R[6:11])*frame_W)-((float(xywh5_1R[18:23])/2)*frame_W)),
        int((float(xywh5_1R[12:17])*frame_H)-((float(xywh5_1R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

        cv2.rectangle(frame, 
        (int((float(xywh5_2R[6:11])*frame_W)-((float(xywh5_2R[18:23])/2)*frame_W)),
        int((float(xywh5_2R[12:17])*frame_H)-((float(xywh5_2R[24:29])/2)*frame_H)),
        int((float(xywh5_2R[18:23]))*frame_W),
        int((float(xywh5_2R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh5_2R[6:11])*frame_W)-((float(xywh5_2R[18:23])/2)*frame_W)),
        int((float(xywh5_2R[12:17])*frame_H)-((float(xywh5_2R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

        cv2.rectangle(frame, 
        (int((float(xywh5_3R[6:11])*frame_W)-((float(xywh5_3R[18:23])/2)*frame_W)),
        int((float(xywh5_3R[12:17])*frame_H)-((float(xywh5_3R[24:29])/2)*frame_H)),
        int((float(xywh5_3R[18:23]))*frame_W),
        int((float(xywh5_3R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh5_3R[6:11])*frame_W)-((float(xywh5_3R[18:23])/2)*frame_W)),
        int((float(xywh5_3R[12:17])*frame_H)-((float(xywh5_3R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

        cv2.rectangle(frame, 
        (int((float(xywh5_4R[6:11])*frame_W)-((float(xywh5_4R[18:23])/2)*frame_W)),
        int((float(xywh5_4R[12:17])*frame_H)-((float(xywh5_4R[24:29])/2)*frame_H)),
        int((float(xywh5_4R[18:23]))*frame_W),
        int((float(xywh5_4R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh5_4R[6:11])*frame_W)-((float(xywh5_4R[18:23])/2)*frame_W)),
        int((float(xywh5_4R[12:17])*frame_H)-((float(xywh5_4R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

        cv2.rectangle(frame, 
        (int((float(xywh5_5R[6:11])*frame_W)-((float(xywh5_5R[18:23])/2)*frame_W)),
        int((float(xywh5_5R[12:17])*frame_H)-((float(xywh5_5R[24:29])/2)*frame_H)),
        int((float(xywh5_5R[18:23]))*frame_W),
        int((float(xywh5_5R[24:29]))*frame_H)),
        (0,0,255), 2)
        cv2.putText(frame, cv_text,
        (int((float(xywh5_5R[6:11])*frame_W)-((float(xywh5_5R[18:23])/2)*frame_W)),
        int((float(xywh5_5R[12:17])*frame_H)-((float(xywh5_5R[24:29])/2)*frame_H))), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.9,
        (0, 0, 255), 2, cv2.LINE_AA)

    else:
        continue
    cv2.imshow("fire_detect_video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    #time.sleep(0.01)