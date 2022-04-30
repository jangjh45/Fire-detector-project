from flask import Flask
from flask import render_template
from flask import Response
from flask_detect import detect
from multiprocessing import Process

app = Flask(__name__)

import flask_detect
import DB_test03

@app.route("/")
def index():
    return render_template("index2.html")



@app.route('/video_feed')
def video_feed():
    return Response(detect(),
        mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__== "__main__":
    process_one = Process(target = flask_detect.detect)
    process_two = Process(target = DB_test03.fire_num)

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()

    app.run(host = '192.168.1.1', port = 50055, debug = True)