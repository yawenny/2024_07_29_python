from flask import Flask
#Flask實體方法建立app
app = Flask(__name__)

#呼叫route實體方法,根目錄,decorator要用@
@app.route("/")
def hello_world():
    return '''<h1>這是python的project</h1>
            <p>這是在codespace環境開發的</p>
            '''