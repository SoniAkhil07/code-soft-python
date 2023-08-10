from flask import Flask,render_template,request,url_for
import random
app=Flask(__name__)
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/pass' ,methods=['POST'])
def form():
    number=int(request.form['num'])
    div=number//3
    if number=="":
        return "<h1>some feilds of form is empty </h1>"
    else:
        password=" "
        for a in range(1,int(div)+1):
            password+=random.choice(LETTERS)
        for b in range(1,int(div)+1):
            password+=random.choice(SYMBOLS)
        for c in range(1,int(div)+1):
            password+=random.choice(NUMBERS)
        passwords=[i for i in password]
        random.shuffle(passwords)
        pas=''.join(passwords)
        return render_template("index.html",password=pas)



if __name__=='__main__':
    app.run()
