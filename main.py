from flask import Flask, request, render_template
from flaskwebgui import FlaskUI
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        code = request.form.get("code")
        # Do something with the code here, such as saving it to a file or processing it further
    return render_template("index.html")


if __name__ == "__main__":
    # If you are debugging you can do that in the browser:
    app.run()
    # If you want to view the flaskwebgui window:
    #FlaskUI(app=app, server="flask").run()
