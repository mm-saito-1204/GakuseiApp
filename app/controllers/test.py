# ホーム画面関連
#
# 最終変更日 2022/07/08
# 変更者　　 Naoki
#

from flask import Blueprint
from flask import render_template, request, redirect;
from app.models.database import User, Post, Tag, FollowList
from sqlalchemy import desc
from app import db, app
from datetime import datetime
import pytz
import os

mod_test = Blueprint('test', __name__, url_prefix='/test')

#
# 1.記事投稿      2.記事更新      3.記事削除 
# 4.アカウント作成 5.アカウント削除
#

#テスト記事投稿
@mod_test.route("/create", methods=["GET", "POST"])
def create():
    title = "TEST"  # タイトル
    body = "TESTデータです"  # 本文
    username = "TESTAccount"  # ニックネーム
    image = ""  # 画像の保存先パス
    tag_1, tag_2, tag_3, tag_4, tag_5 = map(str, "a b c d e".split())  # タグ(スペース区切りで入力してもらう)
    created_at=datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y年%m月%d日 %H時%M分")
    post = Post(title=title, body=body, username=username, created_at=created_at, image=image
            ,tag_1=tag_1, tag_2=tag_2, tag_3=tag_3, tag_4=tag_4, tag_5=tag_5)
    db.session.add(post)
    db.session.commit()
    return redirect("/base/home")

#テスト記事更新
@mod_test.route("/update", methods=["GET", "POST"])
def update():
    postId = 10  # ポストID(通番)
    post = Post.query.get(postId)
    post.title = "TEST!!!!!"  # タイトル
    post.body = "TESTデータです!!!!!"  # 本文
    post.username = "TESTAccount!!!!!"  # ニックネーム
    # post.image = ""  # 画像の保存先パス
    post.tag = "a b c d e"  # タグ(スペース区切りで入力してもらう)
    db.session.add(post)
    db.session.commit()
    return redirect("/base/home")

#テスト記事削除
@mod_test.route("/delete", methods=["GET", "POST"])
def delete():
    postId = 9  # ポストID(通番)
    post = Post.query.get(postId)
    db.session.delete(post)
    db.session.commit()
    return redirect("/base/home")

#テストアカウント作成
@mod_test.route("/signup", methods=["GET", "POST"])
def signup():
    studentNumber = "234567"  # 学籍番号
    username = "TEST2"  # ニックネーム
    password = "1234"  # パスワード
    realname = "テスト2 テスト2"  # 本名
    gender = "女"  # 性別("女", "男", "その他")
    user = User(studentNumber=studentNumber, username=username, password=password, realname=realname, gender=gender)
    db.session.add(user)
    db.session.commit()
    return redirect("/base/home")

#テストアカウント削除
@mod_test.route("/accountDelete", methods=["GET", "POST"])
def accountDelete():
    studentNumber = "234567"  # 学籍番号
    user = User.query.get(studentNumber)
    db.session.delete(user)
    db.session.commit()
    return redirect("/base/home")

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー#

# #投稿画面・アカウント作成画面に役立つ書き方
# @mod_test.route("/mypage", methods=["GET", "POST"])
# def mypage():
#     if request.method == "GET":
#         # GETメソッドの時の処理(そのページに来た時の処理)
#         # 簡単に言うと、そのページを訪れた人にページを表示する処理

#         # ここに処理を書く(DBを取り出しで表示するなど)

#         return render_template("base/mypage.html") #最後はそのページのhtmlを書く

#     elif request.method == "POST":
#         # POSTメソッドの時の処理(そのページで投稿や決定ボタンが押された時など)
#         # 簡単に言うと、入力フォームの情報を受け取ってする処理

#         # ここに処理を書く(DBに書き込んで保存するなど)

#         return redirect("/base/home") # 最後は処理をした後に表示したいURLを書く

#ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー#