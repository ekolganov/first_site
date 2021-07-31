from flask import Flask, render_template, redirect, request

my_app = Flask(__name__)


@my_app.route('/')
@my_app.route('/home')
@my_app.route('/index')
def index():
    return render_template("base.html")


@my_app.route('/main')
def main():
    return render_template("main.html")


@my_app.route('/login')
def login():
    return render_template("login.html")


if __name__ == "__main__":
    my_app.run(port=80, debug=True)



