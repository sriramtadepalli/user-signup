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
    email_error = ""
    temp = ""
        

    if not username or " " in username or len(username) < 3 or len(username) > 20:
        
        username_error = " The username should be between 3 and 20 characters long.  It should not contain a space."

        
 

    if not password or " " in password or len(password) < 3 or len(password) > 20:
        
        password_error = "The password should be between 3 and 20 characters long.  It should not contain a space."
 
        
        


    if password != verifypassword or not verifypassword or " " in verifypassword or len(verifypassword) < 3 or len(verifypassword) > 20:
        
        if password != verifypassword :
            
            if not verifypassword or " " in verifypassword or len(verifypassword) < 3 or len(verifypassword) > 20:
                verifypassword_error = "The Password and Verify Password do not match.  The password should be between 3 and 20 characters long.  It should not contain a space."
            else:
                verifypassword_error = "The Password and Verify Password do not match."
        else:
            verifypassword_error = "The password should be between 3 and 20 characters long.  It should not contain a space."
 
        


    if not "@" in email or not "." in email or " " in email or len(email) < 3 or len(email) > 20:
        
        email_error = "The email should be between 3 and 20 characters long.  It should not contain a space.  It should contain an @ and a '.'"


    if  not username_error:
        if not password_error:
            
            if not verifypassword_error:
                if not email_error:
        
                    template = jinja_env.get_template('hello_form.html')
                    return template.render(email=email, name = username)


    if username_error or password_error or verifypassword_error or email_error:

                    print("In Second if statement")   
                    print(email_error)     
                    template = jinja_env.get_template('username_password_verify_password.html')
                    return template.render(username=username, email=email, username_error = username_error, password_error = password_error, verifypassword_error = verifypassword_error, email_error = email_error)        




 
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)