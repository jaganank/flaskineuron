## Create a simple flask application

from flask import Flask,render_template,request,redirect,url_for

## Create the flask app

app=Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello World!</h2>"

@app.route('/welcome')
def welcome():
    return "Welcome to the Flask Application"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return "The person is passed and score is  "+str(score)

@app.route('/failed/<int:score>')
def failed(score):
    return "The person has failed and score is  "+str(score)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        
    average_marks=(maths+science+history)/3
    result=""
    if average_marks>=50:
        result="success"
    else:
        result="failed"
        
    ##return redirect(url_for(result,score=average_marks))

    
    return render_template('results.html',results=average_marks)



if __name__=='__main__':
    app.run(debug=True)
    



    