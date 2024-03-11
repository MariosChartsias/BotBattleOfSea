from flask import Flask, render_template, request, flash, session, redirect
from py.utils.validations import*  # Adjust the import path
from py.utils.battleOfSeaDAO import*
from py.utils.email_sender import *
from py.utils.crypto import*
from random import randint


app = Flask(__name__)
crypto=Crypto(KEY_1)
app.secret_key = crypto.encrypt('encrypt')  # Set a secret key for flashing messages


# Dictionary to store user data
user_data = {}


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        checkBox = request.form.get('checkBoxTerms') == "on"
        session['checkBoxState'] = checkBox
        
        # Retrieve checkbox state from session or default to False
        checkBox = session.get('checkBoxState', False)
        user_data = {
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'checkBoxTerms': checkBox
        }
        error_message = None

        validator_instance = validations(user_data)
        error_message = validator_instance.fullvalidation(user_data['email'])  # Pass email address only
        if error_message is None:
            databaseAccessMechanism = userDao()
            databaseAccessMechanism.open_session()
            if not databaseAccessMechanism.account_exists(email):
                databaseAccessMechanism.set_personal_data(email, password)
                
                session['activationCode'] = randint(1000,9999)
                session['email'] = user_data['email']
                emailSender = EmailSender(EMAIL_CONSTANT,PASS_CONSTANT)
                emailSender.send_email(user_data['email'],"Please Activate your email address", f'Activation code is {session.get("activationCode")}') 
                return render_template("activation.html")
            else:
                flash("This email has already been registered")
        else:
            flash(error_message)

    return render_template('registration.html', 
                           email=email, 
                           password=password, 
                           confirm_password=confirm_password,
                           checkBox=checkBox)

@app.route('/activate', methods=['POST'])
def activate():
    if request.method == 'POST':
        # Handle activation form submission
        # For example, retrieve activation code from the form and activate the user
        activation_code = request.form['activation_code']

        if(activation_code==str(session.get('activationCode'))):
            databaseAccessMechanism = userDao()
            databaseAccessMechanism.open_session()
            databaseAccessMechanism.activate_email(str(session.get('email')))
            flash("email activated successfully!")
            return render_template("index.html")
        else:  
            flash("wrong activation code")
            
        return render_template('activation.html')
    
# Define a catch-all route to redirect undefined routes to index.html
@app.route('/<path:undefined>', defaults={'undefined': ''})
def catch_all(undefined):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
