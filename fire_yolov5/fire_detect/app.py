from flask import Flask, Response, render_template
from flask_detect import detect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route('/video_feed')
def video_feed():
    return Response(detect(),
        mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__== "__main__":
    app.run(debug = True)