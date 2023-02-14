from flask import Flask, request, render_template, jsonify
from flaskwebgui import FlaskUI
import sqlite_functions
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])

def index():
    database_file = ""
    if request.method == "POST":
        print(request.form.get("database_file"))
        database_file= request.form.get("database_file")
        # Do something with the code here, such as saving it to a file or processing it further
    return render_template("index.html", database_file=database_file)

@app.route("/tables", methods=["GET"])
def tables():
    database_file = request.args.get("database_file")    
    try:
        tables_and_views = sqlite_functions.get_all_tables_info(database_file)       
    except Exception as e:
      #print the error and return an empty dictionary
        print(e)      
        tables_and_views = {}
        

    return jsonify(tables_and_views)
  

if __name__ == "__main__":
    # If you are debugging you can do that in the browser:
    app.run()
    # If you want to view the flaskwebgui window:
    #FlaskUI(app=app, server="flask").run()
