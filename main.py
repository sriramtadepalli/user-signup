import string
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import jinja2
import cgi

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)
 
app = Flask(__name__)

app.config['DEBUG'] = True

 
@app.route("/")
def index():
    template = jinja_env.get_template('username_password_verify_password.html')
    return template.render()
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('username_password_verify_password.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"

    
 
@app.route('/username_password_verify_password.html', methods=['POST'])
def do_admin_login():

    password = request.form['password']
    username = request.form['username']
    verifypassword = request.form['verify_password']
    email = request.form['email']
    username_error = ""
    password_error = ""
    verifypassword_error = ""
    temp = ""
        

    if not username or " " in username or len(username) < 3 or len(username) > 20:
        
        username_error = " Username is wrong."

        
        temp = username_error
        

    else:
        username_correct = "Username is correct."
        temp = username_correct 

    if not password or " " in password or len(password) < 3 or len(password) > 20:
        
        password_error = "password is wrong."
 
        
        
        temp = temp + ' '+ password_error

    else:
        password_correct = "Password is correct."

        temp = temp +" " + password_correct

    if not verifypassword or " " in verifypassword or len(verifypassword) < 3 or len(verifypassword) > 20:
        
        verifypassword_error = "Verify Password is wrong."
 
        
        temp = temp + ' ' + verifypassword_error   

    else:
        verify_password_correct = "Verify Password is Correct."
        
        temp = temp + " " + verify_password_correct
    

    if (password != verifypassword):
        password_validation_error = "Password is not the same as Verify Password."
        #print("Password is not the same as Verify Password.")
        temp =  password_validation_error



    
    template = jinja_env.get_template('username_password_verify_password.html')
    return template.render(name=temp)



 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)