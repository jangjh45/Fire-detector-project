from flask import Flask
from flask import render_template
from flask import Response
import numpy as np
from fire_yolov5.fire_detect.flask_detect import detect
from multiprocessing import Process, Queue

app = Flask(__name__)
import flask_detect

@app.route("/")
def index():
    return render_template("index2.html")



@app.route('/video_feed')
def video_feed():
    return Response(detect(),
        mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__== "__main__":
    flask_detect.detect()
    app.run(debug=True)