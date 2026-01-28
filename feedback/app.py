from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key="supersecret"
@app.route("/", methods=["GET", "POST"])
def feedback():
    if request.method=="POST":
        username=request.form.get("username")
        message=request.form.get("message")
        if not username:
            flash("Username is required")
            return redirect(url_for("feedback"))
        if not message:
            flash("Message is required")
            return redirect(url_for("feedback"))
        flash("Thanks {username}, your feedback has been received!".format(username=username))
        return redirect(url_for("thankyou", username=username, message=message))
    return render_template("feedback.html")
@app.route("/thankyou" , methods=["GET"])
def thankyou():
    username = request.args.get("username")
    message = request.args.get("message")
    return render_template("thankyou.html" ,username=username, message=message)
if __name__ == "__main__":
    app.run(debug=True)