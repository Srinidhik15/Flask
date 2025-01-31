## Building URL Dynamically
### Variable Rules and URL Building

from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return "welcome"

@app.route('/success/<int:score>')   # this has /success as url and append score as an int
def success(score):
    return "the person has passed and marks is " + str(score)
# this is one kind of building url dynamically

@app.route('/fail/<int:score>')  
def fail(score):
    return "the person has failed and marks is " + str(score)

# Result checker
@app.route('/result/<int:marks>')  
def result(marks):
    result = ""
    if marks <50:
        result='fail'
    else:
        result='success'
    #return result     # this will directly give whether it is psuccess or fail
    return redirect(url_for(result,score=marks))  # this will redirect to the 
# success or fail function and give the response


if __name__=="__main__":
    app.run(debug=True)