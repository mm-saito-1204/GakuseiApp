# 投稿のCRUDや投稿画面のルーティングを行う
#
# 最終変更日 2022/07/08
# 変更者　　 Naoki
#

from flask import Blueprint, flash
from flask import render_template, request, redirect;
from flask_login import login_required, current_user
from app.models.database import Post, User
from app import db, app
from werkzeug.utils import secure_filename
import os
from datetime import datetime
import pytz

mod_post = Blueprint('post', __name__, url_prefix='/post')

app_route = os.path.dirname(os.path.abspath(__file__))
app_route = app_route.replace('controllers', '')

#記事投稿画面
@mod_post.route("/create", methods=["GET", "POST"])
@login_required  #ログインしているユーザ以外のアクセスを制限する
def create():
    if request.method == "GET":
        return render_template("post/create.html")
    if request.method == "POST":
        #画像保存処理
        imageExist = False
        if 'file' not in request.files:
            pass
        else:
            file = request.files['file']
            if request.files['file'] == '':
                pass
            elif file and allowed_file(file.filename):
                imageExist = True
                print(request.files['file'])
                filename = secure_filename(file.filename)
                filepath = 'static/image/post/'
                file.save(os.path.join(app_route, filepath ,filename))
        # データベース保存処理
        file = request.files['file']
        file.filename == ''
        title = request.form.get("titleName")
        tag_1, tag_2, tag_3, tag_4, tag_5 = map(str, request.form.get("tags").split())
        body = request.form.get("body")
        created_at=datetime.now(pytz.timezone("Asia/Tokyo")).strftime("%Y年%m月%d日 %H時%M分")
        username = loginUsernameGet(current_user)
        if imageExist:
            image = secure_filename(file.filename)
            post = Post(title=title, body=body, created_at=created_at, username=username
                    ,tag_1=tag_1, tag_2=tag_2, tag_3=tag_3, tag_4=tag_4, tag_5=tag_5, image=image)
        else:
            post = Post(title=title, body=body, created_at=created_at, username=username
                    ,tag_1=tag_1, tag_2=tag_2, tag_3=tag_3, tag_4=tag_4, tag_5=tag_5, image="")
        
        db.session.add(post)
        db.session.commit()
        return redirect("/base/home")


#記事更新画面
@mod_post.route("/<int:postId>/update", methods=["GET", "POST"])
@login_required  #ログインしているユーザ以外のアクセスを制限する
def update(postId):
    post = Post.query.get(postId)
    if request.method == "GET":
        post = Post.query.get(postId)
        return render_template("post/update.html", post = post)
    if request.method == "POST":
        # データベース更新処理
        post.title = request.form.get("titleName")
        tag_1, tag_2, tag_3, tag_4, tag_5 = map(str, request.form.get("tags").split())
        post.tag_1 = tag_1
        post.tag_2 = tag_2
        post.tag_3 = tag_3
        post.tag_4 = tag_4
        post.tag_5 = tag_5
        post.body = request.form.get("body")
        db.session.commit()
        return redirect("/base/home")

#記事削除処理
@mod_post.route("/<int:postId>/delete", methods=["GET", "POST"])
@login_required  #ログインしているユーザ以外のアクセスを制限する
def delete(postId):
    post = Post.query.get(postId)
    db.session.delete(post)
    db.session.commit()
    return redirect("/base/home")

# アップロードファイル拡張子検査 関数
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'psd', 'tiff', 'heic'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ログインユーザのユーザ名取得
def loginUsernameGet(current_user):
    user = str(current_user)
    user = user.replace("<User ", "")
    user = user.replace(">", "")
    user = User.query.get(user)
    return user.username