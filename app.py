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
        if b == "Enter" and q != "":
            return redirect(url_for('search', question=q)) #Redirects you to page to return search results
        else:
            return render_template("home.html")

@app.route("/search/<question>", methods=["GET","POST"])
def search(question):
    urls = utils.get_urls(question) #Sends question to get_urls function in utils.py, which googles query and generates list of suitable urls
    if utils.getqtype(question) == "who":
        names_dict = utils.get_names(urls,question)
    if utils.getqtype(question) == "when":
        names_dict = utils.get_dates(urls)
    number = 0
    for i in names_dict:
        if names_dict[i] > number:
            answer = i
            number = names_dict[i]
    return render_template("search.html", question=question, urls=urls, names_dict=names_dict, answer = answer)

if __name__=="__main__":
    app.debug = True
    app.run(port = 5000)
