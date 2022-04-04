import os
import glob
import time

dir_PATH = 'C:/yolov5-master/runs'
labels_PATH = 'C:/yolov5-master/runs/detect/exp/labels'
txt_PATH = 'C:/yolov5-master/runs/detect/exp/labels/*.txt'

while(True):
    dir_list = os.listdir(dir_PATH)
    dir_count = len(dir_list)
    print(dir_count)
    if dir_count == 0: #폴더가 없으면 아래 코드 무시 1개이상 있으면 아래 코드 실행
        continue
    time.sleep(0.5)
    file_list = os.listdir(labels_PATH)
    file_count = len(file_list)
    print(file_count)
    if file_count == 0: #폴더안에 좌표값txt가 없으면 아래 코드 무시 1개이상 있으면 아래 코드 실행
        continue
    time.sleep(0.5)
    label_list = sorted(glob.glob(txt_PATH), key=os.path.getctime, reverse=True)
    first_list = label_list[0] #label폴더에서 마지막생성 좌표 경로 리스트 저장
    print(first_list)
    
    with open(first_list) as f:   #txt파일을 읽어 각 행 개수 파악
        txt_len = len(f.readlines())
        print(txt_len)
        f.close()
    
    with open(first_list) as y: #txt파일을 읽어 각 행 좌표를 리스트에 저장
        if txt_len == 1:
            xywh1 = y.read().splitlines()
            xywh1_1R = xywh1[0]

            print(xywh1_1R)
            
        elif txt_len == 2:
            xywh2 = y.read().splitlines()
            xywh2_1R = xywh2[0]
            xywh2_2R = xywh2[1]

            print(xywh2_1R)
            print(xywh2_2R)

        elif txt_len == 3:
            xywh3 = y.read().splitlines()
            xywh3_1R = xywh3[0]
            xywh3_2R = xywh3[1]
            xywh3_3R = xywh3[2]

            print(xywh3_1R)
            print(xywh3_2R)
            print(xywh3_3R)

        else:
            continue
        y.close()


