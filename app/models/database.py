# アプリ全体で扱うデータベースの定義ファイル
#
# 最終変更日 2022/07/04
# 変更者　　 Naoki
#

from app import db
from flask_login import UserMixin


#ユーザテーブル User(SQLAlchemy利用)[主キー studentNumber]
# UserMixinでログイン中のアカウント情報を保存(識別)できるようになる
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)             #主キー(flask-login的にidが必要)
    studentNumber = db.Column(db.Integer, unique=True)       #ユニーク制約
    username = db.Column(db.String(30), unique=True)         #ユニーク制約
    password = db.Column(db.String(12))
    realname = db.Column(db.String(30))
    gender = db.Column(db.String(12))

#タグテーブル Tag(SQLAlchemy利用)[主キー tagId]
class Tag(db.Model):
    tagId = db.Column(db.Integer, primary_key=True)  #主キー
    tagName = db.Column(db.String(300))

#記事テーブル Post(SQLAlchemy利用)[主キー postId]
class Post(db.Model):
    postId = db.Column(db.Integer, primary_key=True)                #主キー
    title = db.Column(db.String(50), nullable=False)                #非NULL制約
    body = db.Column(db.String(300), nullable=False)                #非NULL制約
    created_at = db.Column(db.String(30), nullable=False)
    username = db.Column(db.Integer)
    image = db.Column(db.String(300))
    tag_1 = db.Column(db.Integer)
    tag_2 = db.Column(db.Integer)
    tag_3 = db.Column(db.Integer)
    tag_4 = db.Column(db.Integer)
    tag_5 = db.Column(db.Integer)

#フォローリストテーブル FollowList[複合主キー doFollow,beFollow]
class FollowList(db.Model):
    doFollow = db.Column(db.Integer, db.ForeignKey('user.studentNumber'), primary_key=True)  #外部キー
    beFollow = db.Column(db.Integer, db.ForeignKey('user.studentNumber'), primary_key=True)  #外部キー