# 1. Integrate Html with flask
# 2. HTTP Varibles GET & POST

from flask import Flask,redirect,url_for,render_template ,request

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template("index.html")

@app.route('/Pass/<int:score>')
def Pass(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)

@app.route('/Fail/<int:score>')
def Fail(score):
    return "The Person has failed with "+ str(score)

@app.route('/submit',methods = ['POST',"GET"])
def submit():
    total_Score=""

    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_Score=(science+maths+c+data_science)/4
    
    return redirect(url_for("Pass",score=total_Score))



if __name__ =="__main__":
    app.run(debug=True)