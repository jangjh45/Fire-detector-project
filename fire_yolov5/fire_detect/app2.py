from flask import Flask
from flask import render_template
from flask import Response
import threading
from detect_and_db01 import 

app2 = Flask(__name__)



@app2.route("/")
def index():
    return render_template("index.html")



@app2.route('/video_feed')
def video_feed():
    return Response(detect(),
        mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__== "__main__":
    # thread1 = threading.Thread(target = detect)
    # thread2 = threading.Thread(target = fire_num)
    # thread1.start()
    # thread2.start()
    
    app2.run(debug=True)
    