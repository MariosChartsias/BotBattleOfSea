from flask import Flask, render_template, request
from py.utils import validations,directions  # Adjust the import path


app = Flask(__name__)

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
        user_data[email] = {
            'username': username,
            'password': password,
            'confirm_password': confirm_password,
            'checkBoxTerms': checkBox
        }
        


        validator_instance = validations.validations(user_data)
        result = validator_instance.validateData(email)
        redirection_file=directions.redirect(result)

        return render_template(redirection_file, username=username, email=email, password=password, confirm_password=confirm_password)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
