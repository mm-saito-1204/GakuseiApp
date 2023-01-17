# ホーム画面関連
#
# 最終変更日 2022/07/08
# 変更者　　 Naoki
#

from flask import Blueprint
from flask import render_template, request, redirect;
from flask_login import login_required, current_user
from app.models.database import Post, User
from sqlalchemy import desc
from app import db, app

mod_base = Blueprint('base', __name__, url_prefix='/base')

#ホーム画面
@mod_base.route("/home", methods=["GET", "POST"])
@login_required  #ログインしているユーザ以外のアクセスを制限する
def home():
    posts = Post.query.order_by(desc(Post.created_at)).all()
    return render_template("base/home.html", posts=posts, loginUser=loginUsernameGet(current_user))

#マイページ画面
@mod_base.route("/mypage", methods=["GET", "POST"])
@login_required  #ログインしているユーザ以外のアクセスを制限する
def mypage():
    posts = Post.query.filter_by(username=loginUsernameGet(current_user)).order_by(desc(Post.created_at)).all()
    return render_template("base/mypage.html", posts=posts, loginUser=loginUsernameGet(current_user))

#ユーザーページ画面
@mod_base.route("/userpages", methods=["GET", "POST"])
@login_required  #ログインしているユーザ以外のアクセスを制限する
def userpages():
    if request.method == "GET":
        return render_template("base/userpages.html")
    elif request.method == "POST":
        return render_template("base/userpages.html")

#検索結果画面
@mod_base.route("/explore", methods=["GET", "POST"])
@login_required  #ログインしているユーザ以外のアクセスを制限する
def explore():
    if request.method == "GET":
        return render_template("base/explore.html")
    elif request.method == "POST":
        return render_template("base/explore.html")


# ログインユーザのユーザ名取得
def loginUsernameGet(current_user):
    user = str(current_user)
    user = user.replace("<User ", "")
    user = user.replace(">", "")
    user = User.query.get(user)
    return user.username
