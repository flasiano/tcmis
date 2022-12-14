import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("severaccountkey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


from flask import Flask, render_template,request, make_response, jsonify
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>蔡孟潔Python網頁</h1>"
    homepage += "<a href=/mis>MIS</a><br>"
    homepage += "<a href=/today>顯示日期時間</a><br>"
    homepage += "<a href=/welcome?nick=孟潔>傳送使用者暱稱</a><br>"
    homepage += "<a href=/about>孟潔簡介網頁</a><br>"
    homepage += "<a href=/account>表單</a><br>"
    homepage += "<br><a href=/read>讀取Firestore資料</a><br>"

    return homepage

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"
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
@app.route("/read")
def read():
    Result = ""     
    collection_ref = db.collection("PU")    
    docs = collection_ref.order_by("mail", direction=firestore.Query.DESCENDING).get()    
    for doc in docs:         
        Result += "文件內容：{}".format(doc.to_dict()) + "<br>"    
    return Result
@app.route("/webhook", methods=["POST"])
def webhook():
    # build a request object
    req = request.get_json(force=True)
    # fetch queryResult from json
    action =  req.get("queryResult").get("action")
    msg =  req.get("queryResult").get("queryText")
    info = "動作：" + action + "； 查詢內容：" + msg
    return make_response(jsonify({"fulfillmentText": info}))
       


if __name__ == "__main__":
    app.run()
