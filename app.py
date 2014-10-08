from flask import Flask, request, render_template, redirect,session
import search

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="GET":
        return render_template("index.html");
    else:
        b = request.form['b'] #Submit button
        q = request.form['q'] #Type of question
        s = request.form['s'] #The whole question
        if button == "submit" and s != "":
            info = search.search('q','s'); #This gives the other file the query it needs to google and the type of question it is so it can return what we're looking for.
            return render_template("search.html",info = info); #Takes you to page to return search results
        else:
            return render_template("index.html");

if __name__=="__main__":
    app.debug = True
    app.run(port = 5000)
