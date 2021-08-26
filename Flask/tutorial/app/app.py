# Flaskとrender_template（HTMLを表示させるための関数）をインポート
from datetime import datetime
from flask import Flask,render_template,request, session, redirect, url_for
from flask.helpers import url_for
from models import models, database
from models.models import USER_NAME, OnegaiContent
from models.database import MongoDB
from . import key
from hashlib import sha256

# DB
TUTORIAL = 'tutorial'  # DB名
JINJA = 'jinja'  # 願い事コレクション
onegai_db = MongoDB(TUTORIAL, JINJA)
USER = 'user'  # ユーザー情報コレクション
user_db = MongoDB(TUTORIAL, USER)

# Flaskオブジェクトの生成
app = Flask(__name__)
app.secret_key = key.SECRET_KEY

@app.route("/top")
def top():
    status = request.args.get("status")
    return render_template("top.html",status=status)


@app.route("/newcomer")
def newcomer():
    status = request.args.get("status")
    return render_template("newcomer.html",status=status)

# ログイン
@app.route('/login', methods=['post'])
def login():
    # ログイン画面からユーザー名を取得する
    user_name = request.form[models.USER_NAME]
    user_data = user_db.select_user(user_name)
    # ログイン情報を認証する
    if user_data:
        # ログイン画面からパスワードを習得する
        input_password = request.form[models.USER_PASSWORD]
        hashed_password = sha256((user_name + input_password + key.SALT).encode('utf-8')).hexdigest()

        # パスワードを認証
        if hashed_password == user_data[models.USER_PASSWORD]:
            session[models.USER_NAME] = user_name
            return redirect(url_for('index'))
        # パスワード認証できず
        else:
            return redirect(url_for('top', status='wrong_password'))
    # アカウントが見つからなかった
    else:
        return redirect(url_for('top', status='user_notfound'))

# ログアウト
@app.route('/logout')
def logout():
    session.pop(models.USER_NAME, None)
    return redirect(url_for('top', status='logout'))

# ユーザー登録
@app.route("/registar",methods=["post"])
def registar():
    # ログイン画面からユーザー名を取得する
    user_name = request.form[models.USER_NAME]
    user_data = user_db.select_user(user_name)

    # すでに同じユーザー名で登録していたら登録出来ない
    if user_data:
        return redirect(url_for('newcomer', status='exist_user'))
    # 新規登録する
    else:
        input_password = request.form[models.USER_PASSWORD]
        hashed_password = sha256((user_name + input_password + key.SALT).encode('utf-8')).hexdigest()
        data = {
            models.USER_NAME:user_name,
            models.USER_PASSWORD:hashed_password
        }
        user_db.insert_user(data)
        session[models.USER_NAME] = user_name

        return redirect(url_for('index'))

# 「/index」へアクセスがあった場合に、「index.html」を返す
@app.route('/')
@app.route('/index')
def index():
    if models.USER_NAME in session:
        name = session[USER_NAME]
        finds = onegai_db.collection.find()
        onegai_list = database.cursor_2_onegai_list(finds)

        return render_template('index.html', name=name, onegai_list=onegai_list)

    else:
        return redirect(url_for('top', status='logout'))

# テキストと送信ボタンのみの簡単なフォームを受け付ける
@app.route('/index', methods=['post'])
def post():
    name = request.form['name']
    finds = onegai_db.collection.find()
    onegai_list = models.cursor_2_onegai_list(finds)

    return render_template('index.html', name=name, onegai_list=onegai_list)

# お願い記入欄フォームから記入された内容をDBに書き込む
@app.route('/add', methods=['post'])
def add():
    title = request.form[models.WISH_TITLE]
    body = request.form[models.WISH_BODY]
    now = datetime.now()
    content = OnegaiContent(title, body, now)

    onegai_db.insert_one_onegai(content)

    return redirect(url_for("index"))

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

    return redirect(url_for("index"))

# お願いの消去
@app.route("/delete", methods=['post'])
def delete():
    id_list = request.form.getlist("delete")
    from pprint import pprint
    pprint(id_list)

    for id in id_list:
        onegai_db.delete_one_onegai(id)

    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)