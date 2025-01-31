from flask import Flask

app=Flask(__name__)   # this is a WSGI application

#Decorator
@app.route('/')   # default function
def welcome():
    return "welcome here..."  # when we go to the app route page welcome function is triggered automatically

# here the main function above name and below func name should always be different
@app.route('/members')
def members():
    return "hi how are you?"  # this is another function so if we write /members to the existing url link it gives the message from the function



if __name__=="__main__":
    app.run(debug=True)   # when we put debug=True and update the function it will change accordingly