from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def login():
    return render_template("login.html")
@app.route("/submit", methods=["POST"])
def submit():
    username=request.form.get("username")
    password=request.form.get("password")
    # if username=="arnab2004" and password=="2004":
    #     return render_template("welcome.html",name=username)
    valid_users={
        "admin":"123",
        "user1":"pass1",
        "user2":"pass2",
        "arnab": "2004"
    }
    if username in valid_users and password==valid_users[username]:
        return render_template("welcome.html",name=username)
    else:
        return "Invalid credentials. Try again..."
if __name__ == "__main__":
    app.run(debug=True)