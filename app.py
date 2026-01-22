from flask import Flask
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
if __name__ == "__main__":
    app.run(debug=True)  