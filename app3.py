# 1. Integrate Html with flask
# 2. HTTP Varibles GET & POST

from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template("index.html")

if __name__ =="__main__":
    app.run(debug=True)