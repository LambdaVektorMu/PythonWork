# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from datetime import datetime
from flask import Flask,render_template,request
from models import models, database
from models.models import OnegaiContent
from models.database import MongoDB

# DB
TUTORIAL = 'tutorial'  # DB名
JINJA = 'jinja'  # 願い事コレクション
onegai_db = MongoDB(TUTORIAL, JINJA)

# Flaskオブジェクトの生成
app = Flask(__name__)

# 「/index」へアクセスがあった場合に、「index.html」を返す
@app.route('/')
@app.route('/index')
def index():
    name = request.args.get('name')
    finds = onegai_db.collection.find()
    onegai_list = database.cursor_2_onegai_list(finds)

    return render_template('index.html', name=name, onegai_list=onegai_list)

# テキストと送信ボタンのみの簡単なフォームを受け付ける
@app.route('/index', methods=['post'])
def post():
    name = request.form['name']
    finds = onegai_db.collection.find()
    onegai_list = cursor_2_onegai_list(finds)

    return render_template('index.html', name=name, onegai_list=onegai_list)

# お願い記入欄フォームから記入された内容をDBに書き込む
@app.route('/add', methods=['post'])
def add():
    title = request.form[models.WISH_TITLE]
    body = request.form[models.WISH_BODY]
    now = datetime.now()
    content = OnegaiContent(title, body, now)

    onegai_db.insert_one_onegai(content)

    return index()

# お願いの更新
@app.route("/upload", methods=['post'])
def update():
    # 選択した願い事
    id = request.form['update']
    content = onegai_db.select_one_onegai(id)

    # 入力した新しい項目
    new_title = request.form[models.WISH_TITLE]
    new_body = request.form[models.WISH_BODY]
    now = datetime.now()
    if new_title:
        content[models.WISH_TITLE] = new_title
    if new_body:
        content[models.WISH_BODY] = new_body

    # DBの更新
    if new_title or new_body:
        content[models.WISH_DATETIME] = now
        onegai_db.update_one_onegai(content)

    return index()

# お願いの消去
@app.route("/delete", methods=['post'])
def delete():
    id_list = request.form.getlist("delete")
    from pprint import pprint
    pprint(id_list)

    for id in id_list:
        onegai_db.delete_one_onegai(id)

    return index()

if __name__ == '__main__':
    app.run(debug=True)