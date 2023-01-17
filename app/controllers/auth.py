# アカウント関連の画面操作やルーティングを行う
#
# 最終変更日 2022/07/19
# 変更者　　 Marin
#

from flask import Blueprint
from flask import render_template, request, redirect, flash;
from flask_login import LoginManager, login_user, logout_user, login_required
from app import db, app
from app.models.database import User

#ログインマネージャー生成
login_manager = LoginManager()
login_manager.init_app(app)
#最新時点のユーザ情報を読み取る
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

#ログイン処理
@mod_auth.route("/login", methods=["GET","POST"])
def login():
    #画面アクセス時の処理
    if request.method == "GET":
        return render_template("auth/login.html")
    #ログイン時の処理
    if request.method == "POST":
        studentNumber_check = request.form.get("studentNumber") #学籍番号取得
        password_check = request.form.get("password")  #パスワード取得
        #学籍番号の文字数による正誤判定
        if(len(studentNumber_check) != 6):
            flash("学籍番号を正しく入力してください")
            return redirect("/auth/login")
        user = User.query.filter_by(studentNumber=studentNumber_check).first()
        #アカウント存在判定
        if(user is None):
            flash("学籍番号もしくはパスワードが間違っています")
            return redirect("/auth/login")
        #学籍番号&パスワード照合
        getstudentNumber = user.studentNumber
        getpassword = user.password
        print(getstudentNumber)
        print(studentNumber_check)
        print(getpassword)
        print(password_check)
        if(str(password_check) == str(getpassword) and str(studentNumber_check) == str(getstudentNumber)):
            login_user(user)
            return redirect("/base/home")
        else:
            flash("学籍番号もしくはパスワードが間違っています")
            return redirect("/auth/login")


#サインアップ
@mod_auth.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("auth/signup.html")
    if request.method == "POST":
        form_studentNumber = request.form.get("studentNumber") #request.form.get()でHTMLからデータを受け取り変数に保存
        form_password  = request.form.get("password")
        form_username  = request.form.get("username")
        form_realname  = request.form.get("lastname") + request.form.get("firstname")
        form_gender    = request.form.get("gender")
        #アカウント作成可能判定 
        accountFlg = False
        user = User.query.get(form_studentNumber)
        if user is not None:  #アカウント存在判定
            accountFlg = True
            flash("この学籍番号はすでに使用されています")
        if(len(form_studentNumber) != 6):  #学籍番号の文字数による正誤判定
            accountFlg = True
            flash("学籍番号を正しく入力してください")
        #パスワードの文字と文字数による正誤判定
        if(len(form_password) < 7  #7文字以下
                or not any(map(str.isdigit, form_password))  #数字が入っている
                or not any(map(str.isalpha, form_password))):#アルファベットが入っている
            accountFlg = True
            flash("パスワードには英数字を組み合わせた7文字以上の文字列を設定してください")
        if(accountFlg):
            return redirect("/auth/signup")
        #ユーザ登録処理
        user = User(studentNumber = form_studentNumber, password = form_password
                ,username = form_username, realname = form_realname, gender = form_gender)
        db.session.add(user)
        db.session.commit()
        return redirect('/auth/login')


#ログアウト
@mod_auth.route("/logout", methods=["GET","POST"])
@login_required  #ログインしているユーザ以外のアクセスを制限する
def out():
    logout_user()
    return redirect("/auth/login")


#ログイン必須画面に非ログイン状態でアクセスした際の処理
@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/auth/login')