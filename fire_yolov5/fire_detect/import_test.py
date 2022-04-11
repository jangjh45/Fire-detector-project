from client_cv2 import detect
import threading


if __name__ == '__main__':
    my_thread = threading.Thread(target=detect)
    my_thread.start()