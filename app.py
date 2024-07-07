from flask import Flask

app = Flask(__name__) #-----WSGI app ,this is a standard to communicate between the server and application

@app.route('/')#----------decorator for defining the url
def welcome():
    return "Welcome home happy son"

@app.route('/member')
def member():
    return "memeber"

if __name__ =="__main__":
    app.run(debug=True) #-----debug is true means that any time we do changes the server is automaticaly restarted