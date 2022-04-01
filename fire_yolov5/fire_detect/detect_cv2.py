import os
import cv2
import glob

file_path = 'C:/label'
file_names = os.listdir(file_path)
i = 0

for name in file_names:
    src = os.path.join(file_path, name)
    dst = str(i) + '.txt'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
















input_dir = 'C:/lable/'
f = open('')
