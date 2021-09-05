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
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator defines the   
def home():  
    return "hello, this is our first flask website";  # semicolone very important
@app.route("/about")
def about():
    return "aboutpage from flask framework";
  
if __name__ =='__main__':  
    app.run(debug = True,port=9000)  

# press ctrl+url:port in terminal to open the webpage


