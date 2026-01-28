from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def feedback():
    if request.method=="POST":
        username=request.form.get("username")
        message=request.form.get("message")
        return render_template("thankyou.html", username=username, message=message)
    return render_template("feedback.html")
if __name__ == "__main__":
    app.run(debug=True)