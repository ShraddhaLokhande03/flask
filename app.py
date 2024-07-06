from flask import Flask

app = Flask(__name__) #-----WSGI app ,this is a standard to communicate between the server and application

@app.route('/')
def welcome():
    return "Welcome"

if __name__ =="__main__":
    app.run()