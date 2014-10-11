from flask import Flask, request, render_template, redirect, session, url_for
import utils

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/home")
def home():
    if request.method=="GET":
        return render_template("home.html")
    else:
        b = request.form['b'] #Submit button
        q = request.form['q'] #The question
        if b == "enter" and q != "":
            return redirect(url_for('search', question=q)) #Redirects you to page to return search results
        else:
            return render_template("home.html")

@app.route("/search/<question>", methods=["GET","POST"])
def search(question):
    info = utils.getinfo(question)
    return render_template("search.html", question=question, info=info)

if __name__=="__main__":
    app.debug = True
    app.run(port = 5000)
