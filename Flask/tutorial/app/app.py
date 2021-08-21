# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from re import X
from flask import Flask,render_template,request
from models.models import OnegaiContent
from models.database import MongoDB


# Flaskオブジェクトの生成
app = Flask(__name__)

# 「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/")
@app.route("/index")
def index():
    name = request.args.get('name')
    db = MongoDB('tutorial', 'jinja')
    onegai_list = db.collection.find()
    return render_template('index.html', name=name, onegai_list=onegai_list)

# テキストと送信ボタンのみの簡単なフォームを受け付ける
@app.route("/index", methods=["post"])
def post():
    name = request.form["name"]
    db = MongoDB('tutorial', 'jinja')
    onegai_list = db.collection.find()
    return render_template('index.html', name=name, onegai_list=onegai_list)

if __name__ == "__main__":
    app.run(debug=True)