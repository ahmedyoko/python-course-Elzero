from flask import Flask , render_template
skills_app = Flask(__name__)

my_skills = [('Html',80),('Css',75),('python',95),('MySql',45)]


@skills_app.route("/")
def homepage():
    return render_template("homepage_extend.html",
                            pagetitle="Home",
                            custom_css="home"); # all in the template appear whatever you put in head or body e.g test="hello A " but in body


@skills_app.route("/add")
def add():
    return render_template("add.html",
                            pagetitle="Add Skill",
                            custom_css="add");


@skills_app.route("/about")
def ab():
    return render_template("about_extend.html",pagetitle="About us");

@skills_app.route("/skills")
def skills():
    return render_template("skills.html",
                            pagetitle="My Skills",
                            page_head="My Skills",
                            description="This My Skill Page",
                            skills=my_skills,
                            custom_css="skills");
# skills=my_skills => assign to variable


if __name__=="__main__" :
    skills_app.run(debug=True,port=8000)