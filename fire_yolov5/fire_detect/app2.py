from flask import Flask
from flask import render_template
from flask import Response
from flask_detect import detect
from DB_test03 import fire_num
from multiprocessing import process

app2 = Flask(__name__)



@app2.route("/")
def index():
    return render_template("index.html")



@app2.route('/video_feed')
def video_feed():
    return Response(detect(),
        mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__== "__main__":
    process_one = process(target = detect)
    process_two = process(target = fire_num)

    process_one.start()
    process_two.start()
    
    app2.run(debug=True)
    