from flask import Flask, request
app=Flask(__name__)
@app.route("/")
def home():
    return "Hello, World!"
@app.route("/about")
def about():
    return "this is the about page."
@app.route("/contact")
def contact():
    return "this is the contact page."
#methods GET and POST
@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        return "you are sending data"
    else:
        return "you are viewing data"
if __name__ == "__main__":
    app.run(debug=True)  
