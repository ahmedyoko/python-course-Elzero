from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
@app.route("/about")
def about():
    return "aboutpage from flask framework"

if __name__ == "__main__":
    app.run(port=900)