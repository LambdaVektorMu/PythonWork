# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from datetime import datetime
from flask import Flask,render_template,request
from pymongo import cursor
from models.models import OnegaiContent
from models.database import MongoDB


# Flaskオブジェクトの生成
app = Flask(__name__)

def cursor_2_onegai_list(cur):
    onegai_list = []
    for c in cur:
        d = {}
        d['title'] = c['title']
        d['body'] = c['body']
        if 'date' in c and type(c['date']) is datetime:
            d['date'] = c['date'].strftime('%Y年%m月%d日 %H:%M:%S')
        else:
            d['date'] = '未設定'
        onegai_list.append(d)

    return onegai_list

# 「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/")
@app.route("/index")
def index():
    name = request.args.get('name')
    db = MongoDB('tutorial', 'jinja')
    finds = db.collection.find()
    onegai_list = cursor_2_onegai_list(finds)

    return render_template('index.html', name=name, onegai_list=onegai_list)

# テキストと送信ボタンのみの簡単なフォームを受け付ける
@app.route("/index", methods=["post"])
def post():
    name = request.form["name"]
    db = MongoDB('tutorial', 'jinja')
    finds = db.collection.find()
    onegai_list = cursor_2_onegai_list(finds)

    return render_template('index.html', name=name, onegai_list=onegai_list)

# お願い記入欄フォームから記入された内容をDBに書き込む
@app.route("/add", methods=["post"])
def add():
    db = MongoDB('tutorial', 'jinja')

    title = request.form["title"]
    body = request.form["body"]
    now = datetime.now()
    content = OnegaiContent(title, body, now)

    db.insert_one_onegai(content)

    return index()

if __name__ == "__main__":
    app.run(debug=True)