from flask import Flask, request, redirect, url_for, session, Response
app=Flask(__name__)
app.secret_key="supersecret"
#login page
@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username= request.form.get("username")
        password=request.form.get("password")
        if username=="admin" and password=="123":
            session["user"]=username #stores username in the session
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again...",mimetype="text/plain") #response type will be text
    return '''
<h2>Login Page</h2>
<form method="POST">
username: <input type="text" name="username"><br>
Password: <input type="text" name="password"><br>
<input type="submit" value="login">
</form>
'''
# welcome route

@app.route("/welcome",methods=["GET","POST"])
def welcome():
    if "user" in session:
        return f'''
<h2>Welcome, {session["user"]}!!<h2>
<a href={url_for('logout')}>Logout</a>
'''
    return redirect(url_for("login"))

# logout route

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)