from flask import Flask, render_template, request,session,redirect,url_for,g
from src.core import model

app = Flask(__name__)
#puedo generarlo de manera random
app.secret_key = 'bruceBruno'

username = ''
user = model.check_users()

@app.route('/',methods = ['GET'])
def home():

    if 'username' in session:
        g.user=session['username']
        return render_template('football.html', message = '<img src=static/img/diego.jpg></>')
    return render_template('homepage.html', message = 'Login to the page or sing up!')


@app.route('/login',methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        areyouuser= request.form['username']
        pwd = model.check_pw(areyouuser)
        if request.form['password'] == pwd:
            session['username'] = request.form['username']
            return redirect(url_for('home'))
    return render_template('index.html')

"""    if request.method == 'GET':
        return render_template('index.html', message="Welcome to my WebAPP TODO Bruce.")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if model.get_user(username,password):
            message = "Welcome to your ToDo list!"
            return render_template("dashboard.html", message = message)
        else:  
            error_message = "This is not a valiid user."
            return render_template("index.html",message = error_message)"""

@app.route('/sing-up',methods = ['GET', 'POST'])
def singup():
    if request.method == 'GET':
        return render_template('singup.html', message="Enter a valid email & a password.")
    else:
        username = request.form["username"]
        password = request.form["password"]
        if model.add_user(username,password):
            message="The user was created succesfully."
            return render_template("index.html", message = message)
        else:  
            error_message = "There is an user in the database with the same username."
            return render_template("singup.html",message = error_message)

@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']
        
"""@app.route('/football',methods = ['GET'])
def football():
    return render_template('football.html')"""

@app.route('/about',methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/privacy',methods = ['GET'])
def privacy():
    return render_template('privacy.html')

@app.route('/terms',methods = ['GET'])
def terms():
    return render_template('terms.html')

@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port = 7000, debug = True)