from flask import Flask, render_template,request
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>蔡孟潔Python網頁</h1>"
    homepage += "<a href=/mis>mis相關工作介紹</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=孟潔>傳送使用者暱稱</a><br>"
    homepage += "<a href=/about>孟潔簡介網頁</a><br>"
    homepage += "<a href=/account>表單</a><br>"
    return homepage

@app.route("/mis相關工作介紹")
def course():
    return render_template("管理導論.html")
@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html", datetime = str(now))
@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("nick")
    return render_template("welcome.html", name=user)
@app.route("/i")
def aboutme2():
    return render_template("aboutme2.html")
@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")        


if __name__ == "__main__":
    app.run()
