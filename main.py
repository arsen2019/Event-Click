# from flask import render_template, url_for, request, redirect
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
#
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     mail = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     date = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return '<User %r>' % self.id
#
# # class Article(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     title = db.Column(db.String(100), nullable=False)
# #     intro = db.Column(db.String(300), nullable=False)
# #     text = db.Column(db.Text, nullable=False)
# #     date = db.Column(db.DateTime, default=datetime.utcnow)
# #
# #     def __repr__(self):
# #         return '<Article %r>' % self.id
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/sign_up', methods=['POST', 'GET'])
# def about():
#     if request.method == 'GET':
#         return render_template('sign_up.html')
#     mail = request.form['mail']
#     password = request.form['password']
#     print(request.headers)
#
#
#     user = User(mail=mail, password=password)
#     try:
#         db.session.add(user)
#         db.session.commit
#         return redirect('/')
#     except:
#         return "Something went wrong while entering.Please try again later."
#
# @app.route('/login')
# def posts():
#     return render_template('login.html')
#
#
# if __name__ == "__main__":
#     app.run(debug=True)

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)