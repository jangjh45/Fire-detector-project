import os
import cv2
import glob
from rmfile import *     #이전 detect파일 삭제
import time

rtsp_PATH = 'rtsp://192.168.1.202:8555/unicast'
labels_PATH = 'C:/yolov5-master/runs/detect/exp/labels'
txt_PATH = 'C:/yolov5-master/runs/detect/exp/labels/*.txt'


#cap = cv2.VideoCapture(rtsp_PATH)

while(True):
    file_list = os.listdir(labels_PATH)
    file_count = len(file_list)
    #print(file_count)
    if file_count == 0: #폴더안에 좌표값txt가 없으면 아래 코드 무시 1개이상 있으면 아래 코드 실행
        continue

    # i = 1 
    # for name in file_list:  #txt파일 이름 새로 지정
    #     src = os.path.join(rename_PATH, name)
    #     dst = str(i) + '.txt'
    #     dst = os.path.join(rename_PATH, dst)
    #     os.rename(src, dst)
    #     i += 1

    label_list = sorted(glob.glob(txt_PATH), key=os.path.getctime, reverse=True)
    first_list = label_list[0]
    #print(first_list)
    
    with open(first_list) as f:   #파일을 읽어 각 행을 리스트에 저장
        xywh = f.read().splitlines()
        print(xywh)
        time.sleep(1)
