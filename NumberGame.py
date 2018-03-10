# pylint: disable=print-statement

from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "Dontouch"
@app.route("/")
def NumberGame():
    return render_template("NumberGame.html")

@app.route("/userguess", methods = ["POST"])
def UserGuess():
    user = request.form['guess']
    print "user", user
    user = int(user)
    if type(user) == int:
        print "user is int"
    computer = random.randrange(1,101)
    session["result"] = computer
    print "comp", session["result"]
    if type(session["result"]) == int:
        print "computer is integer"
    if computer < user:
        print user, "Too High!"
        session["prompt"] = "Too High!"
    elif computer > user:
        print user, "Too Low!"
        session["prompt"] = "Too Low!"
    elif computer == user:
        print "win"
        session["prompt"] = "was the Number!"
    return redirect("/")

@app.route("/restart", methods = ["POST"])
def Restart():
    session.pop("result")
    session.pop("prompt")
    return redirect("/")
app.run(debug=True)