from flask import Flask, render_template, session, redirect, url_for
from database import db
from flask_restful import Api
from flask_session import Session
from resources import routes

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "host": "mongodb://localhost:27017/road",
}
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False
app.secret_key = "kahga/a;r4rra12"
Session(app)
db.init_db(app)
api = Api(app)
routes.init_routes(api)


@app.route('/admin')
def admin():
    return render_template("login.html")


@app.route("/admin/dashboard")
def dashboard():
    if session.get("admin"):
        return render_template("admin/dashboard.html")
    return redirect(url_for('admin'))


@app.route("/admin/questions")
def questions():
    if session.get("admin"):
        return render_template("admin/questions-dashboard.html")
    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run()
