import threading
from flask import Flask, Response, render_template
from detect_and_db01 import detect, fire_num

app2 = Flask(__name__)

@app2.route("/")
def index():
    return render_template("index.html")

@app2.route('/video_feed')
def video_feed():
    return Response(detect(),
        mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__== "__main__":
    thread1 = threading.Thread(target=fire_num)
    thread1.start()
    app2.run(host="0.0.0.0", port="50050")