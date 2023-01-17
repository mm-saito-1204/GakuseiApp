# タイトル・概要
学生用SNS Webアプリケーション(Python・Flask) 

**「studentPLAN」**

プログラミングサークルで、２週間で成果物を作ろうという企画で作成したWebアプリケーションです。
初めてのWebアプリケーション構築ですのでバグ等ありますが、是非ご覧ください。

## イメージ画像
### 会員登録ページ
<img width="1440" alt="スクリーンショット 2023-01-17 13 22 49" src="https://user-images.githubusercontent.com/107006861/212816446-5af70c83-053a-4820-8ba8-6d9044bb5b15.png">

### ログインページ
<img width="1440" alt="スクリーンショット 2023-01-17 13 22 40" src="https://user-images.githubusercontent.com/107006861/212816510-9b3481b5-e9de-4c20-ae03-bbb1690ef1ef.png">

### トップページ
<img width="1439" alt="スクリーンショット 2023-01-17 13 50 18" src="https://user-images.githubusercontent.com/107006861/212816420-fccaf9a8-49d1-4168-9b78-ea77c048e16f.png">


### 投稿ページ
<img width="1439" alt="スクリーンショット 2023-01-17 14 28 18" src="https://user-images.githubusercontent.com/107006861/212817357-1dcdb16b-129c-4037-9c32-05bfc70ef0d5.png">


## 使用技術
- Python 3.9.6(venv)
- Flask 2.1.2
- Flask-Bootstrap 3.3.7.1
- Jinja2 3.1.2
- sqLite 3.37.0

## 機能一覧
- ユーザー登録機能
- ログイン・ログアウト機能
- 投稿機能
- 記事更新機能
- 記事削除機能
- 画像投稿
- 画像投稿プレビュー
- マイページ

## 実行方法
- venv(Python 3.9.6)を作成し、 requirements.txt を pip install する
- run.py を実行する
- 会員登録ページへアクセスし、会員登録をする(http://localhost:5000/auth/signup)
- ログインする

## アピールポイント
- *企画から発表までの期間が２週間* かつ *初めてのWebアプリケーション構築*
という条件のもとで三人チームで開発したWebアプリケーションです。

- 勉強時間を含めて２週間での開発だったので、想定していた機能のなかでもページを作成していないページがあります。

- FlaskのBlueprintを使用し、ログイン・投稿・その他の処理でファイルを分けました。そうすることで、可読性を高めました。
