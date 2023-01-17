# appフォルダ(アプリ全体)で扱う変数等の設定ファイル
#
# 最終変更日 2022/07/13
# 変更者　　 Naoki
#

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
UPLOAD_FOLDER = '/static/image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
#データベース生成（連携）
db = SQLAlchemy(app)

# Sample HTTP error handling
# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.controllers.auth import mod_auth
from app.controllers.post import mod_post
from app.controllers.base import mod_base
from app.controllers.test import mod_test
# Register blueprint(s) ブループリントの設定
app.register_blueprint(mod_auth)
app.register_blueprint(mod_post)
app.register_blueprint(mod_base)
app.register_blueprint(mod_test)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()