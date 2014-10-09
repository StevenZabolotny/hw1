from flask import Flask, request, render_template, redirect,session
import search

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/home")
def home():
    button = request.args.get("b",None)
    question = request.args.get("q",None)
    if request.method=="GET" or button==None or (button!=None and question==None):
        return render_template("home.html");
    else:
        b = request.form['b'] #Submit button
        q = request.form['q'] #Type of question
        s = request.form['s'] #The whole question
        if button == "submit" and s != "":
            info = search.search('q','s'); #This gives the other file the query it needs to google and the type of question it is so it can return what we're looking for.
            return render_template("search.html",info = info); #Takes you to page to return search results
        else:
            return render_template("home.html");

@app.route("/search")
def search():
    return render_template("search.html")

if __name__=="__main__":
    app.debug = True
    app.run(port = 5000)
