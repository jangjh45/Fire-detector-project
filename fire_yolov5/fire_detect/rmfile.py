import os
import shutil
import time

rmfile_PATH = 'C:/yolov5-master/runs/detect/exp'

if os.path.exists(rmfile_PATH):
    shutil.rmtree(rmfile_PATH)

time.sleep(10)