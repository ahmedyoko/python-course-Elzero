from flask import Flask
app = Flask(__name__)
@app.route('/')
def ahmed():
    return "hello flask"
@app.route('/about')
def about():
    return "about"
if __name__=='__main__':
    app.run(debug=True,port=9000)