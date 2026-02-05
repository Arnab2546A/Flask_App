from flask import Flask, render_template, redirect, url_for, flash, session
from form import RegistrationForm
app = Flask(__name__)
app.secret_key="supersecret"
@app.route("/", methods=["GET", "POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        session["registered"] = True
        flash(f"Welcome, {name} ! You have registered Successfully", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    if not session.get("registered"):
        flash("Please register first.", "error")
        return redirect(url_for("register"))
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)