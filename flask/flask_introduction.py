#-----------------------------------------------------------
#------Flask Introduction and your First Page------
#-----------------------------------------------------------
#-----Flask is Microframework built with python-------------
#-----------------------------------------------------------
#---HTML
#---CSS
#---javaScript
# -----------------------------------------------------------
from flask import Flask
app = Flask(__name__)
@app.route("/")
def homepage():
    return 'Hello from flask framework'
@app.route("/about")
def about():
    return "aboutpage from flask framework"
if __name__== "___main__":
    app.run()


