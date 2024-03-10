from flask import Flask, render_template, request, flash
from py.utils.validations import*  # Adjust the import path
from py.utils.battleOfSeaDAO import*
from py.utils.directions import redirect



app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flashing messages

# Dictionary to store user data
user_data = {}  

@app.route('/')
def main():
    return render_template('registration.html')

@app.route('/register', methods=['POST'])

def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirmPassword']
        checkBox= request.form.get('checkBoxTerms')=="on"
        
        # Add user data to the dictionary
        user_data = {
            'email' : email,
            'username': username,
            'password': password,
            'confirm_password': confirm_password,
            'checkBoxTerms': checkBox
        }
        error_message=None

        validator_instance = validations(user_data)
        error_message = validator_instance.fullvalidation(user_data['email'])  # Pass email address only
        if error_message is None:
            databaseAccessMechanism = userDao()
            databaseAccessMechanism.open_session()
            if not databaseAccessMechanism.account_exists(email):
                databaseAccessMechanism.set_personal_data(email, password, 12324)
            redirection_file = redirect(True)
            return render_template(redirection_file, username=username, email=email, password=password, confirm_password=confirm_password)
        else:
            flash(error_message)
            if(checkBox): checkBox="on"
            return render_template('registration.html', 
                           username=username, 
                           email=email, 
                           password=password, 
                           confirm_password=confirm_password,
                           checkBox=checkBox)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
