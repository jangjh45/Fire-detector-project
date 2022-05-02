from flask import Flask
from flask import render_template
from flask import Response
import threading
from flask_detect import detect
from DB_test03 import fire_num

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")



@app.route('/video_feed')
def video_feed():
    return Response(detect(),
        mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__== "__main__":
    process_one = threading.Thread(target = detect)
    process_two = threading.Thread(target = fire_num)

    process_one.start()
    process_two.start()

    app.run(debug = True)