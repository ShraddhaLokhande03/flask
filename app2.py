# Building URL Dynamically
# Variable Rules and URL Building

from flask import Flask,redirect,url_for
app = Flask(__name__)

# @app.route('/')
# def Welcome():
#     return "good morning"

@app.route('/Pass/<int:score>')
def Pass(score):
    return "<html><body><h1>The Person has passed with</h1></body><html>"

@app.route('/Fail/<int:score>')
def Fail(score):
    return "The Person has failed with "+ str(score)

@app.route('/result/<int:marks>')
def result(marks):
    result = ""
    if marks>=40:
        result="Pass"
    else:
       result = "Fail"
    return redirect(url_for(result,score=marks))
    
if __name__ =="__main__":
    app.run(debug=True)
