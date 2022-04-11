from flask import Flask
from flask import render_template
from flask import Response
import numpy as np
import threading

app2 = Flask(__name__)

from rmfile import *
from flask_detect import detect



@app2.route("/")
def index():
    return render_template("index.html")



@app2.route('/video_feed')
def video_feed():
    return Response(detect(),
        mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__== "__main__":
    app2.run(debug=True)
    # my_thread = threading.Thread(target=detect())
    # my_thread.start()