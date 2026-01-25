from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def student_profile():
    return render_template("profile.html", name="Arnab",subjects=["Math","Science","History"],age=21,is_topper=True)
if __name__ == "__main__":
    app.run(debug=True)