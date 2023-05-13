from distutils.log import debug
from pickle import TRUE
from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


app = Flask(name)
app.secret_key = "test" #make the secret key more secure later
app.permanent_session_lifetime = timedelta(days=7)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route("/")
def home():
    return render_template("index.html"), f"TEST TEST"

@app.route("/<id>")
def CVE(id):
    #TODO:button for CVE list
    #TODO:CVE's redirects to CVE id page with stats
    return  render_template("index.html"), f"This is the vulnerability {id}" #Directs you to a id input. For example /CVE-123

@app.route("/admin")
def admin():
    return redirect(url_for("home")) # Redirects the user to the front page

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("home"))
    else:
        if "user" in session:
            return redirect(url_for("home"))
        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/VulnStats")
def testframe():
    #urls =['<iframe src="http://localhost:5601/goto/9164b550-d201-11ed-81d2-55f73385f722"</iframe>'] 
    return render_template("visual.html")

@app.route("/Help")
def help():
    return render_template("hjelpe.html")


@app.route("/MakeVisual")
def MakeVis():
    return render_template("MakeVisual.html")

@app.route("/OtherVisual")
def OtherVis():
    return render_template("OtherVisual.html")

# defining the home page of our site
if name == "main":
    app.run(debug=TRUE)