from flask import Flask
#Flask實體方法建立app
app = Flask(__name__)

#呼叫route實體方法,根目錄,decorator要用@
@app.route("/")
def hello_world():
    return "<h1>星期三,robert您好!</h1>"#html字串