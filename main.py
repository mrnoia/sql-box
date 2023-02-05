from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form.get("code")
        # Do something with the code here, such as saving it to a file or processing it further
    return render_template("ace.html")


if __name__ == "__main__":
    app.run()
