from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template('homepage.html',
                            pagetitle="Home Page",
                            custom_css='home')
@app.route('/add')
def add():
    return render_template('add.html',
                            pagetitle="Add Skill",
                            custom_css='add')
@app.route('/about')
def about():
    return render_template('about.html',pagetitle="About us")
if __name__=='__main__':
    app.run(debug=True,port=9000)
