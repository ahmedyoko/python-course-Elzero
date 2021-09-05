#-----------------------------------------------------------
#------Flask => Create HTML file
#-----------------------------------------------------------
from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def homepage():
    return render_template("homepage.html",pagetitle="Home");
@app.route("/about")
def ab():
    return render_template("about.html",pagetitle="About us");
if __name__=="__main__" :
    app.run(debug=True,port=9000)