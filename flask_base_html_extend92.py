#..................................................
# Flask => Create and extend html template
#..................................................
# page of html has 2 parts :
# 1- static : which share with other page(structure) 
# 2- dynamic : differ between page and another as the content in 
# .................................................
# base page => making all static part of html pages in one place to be easy handle
# .................................................
from flask import Flask , render_template
skills_app = Flask(__name__)
@skills_app.route("/")
def homepage():
    return render_template("homepage_extend.html",pagetitle="Home"); # all in the template appear whatever you put in head or body e.g test="hello A " but in body
@skills_app.route("/about")
def ab():
    return render_template("about_extend.html",pagetitle="About us");
if __name__=="__main__" :
    skills_app.run(debug=True,port=8000)