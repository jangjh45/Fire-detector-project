from multiprocessing import process
from flask import Flask, Response, render_template
from detect_and_db01 import fire_num, detect

app2 = Flask(__name__)

@app2.route("/")
def index():
    return render_template("index.html")



@app2.route('/video_feed')
def video_feed():
    return Response(detect(),
        mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__== "__main__":
    process1 = process(target = fire_num, )
    process1.start()
    
    app2.run(debug=True)
    
    