from flask import Flask, render_template, request

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
        

        # Add user data to the dictionary
        user_data[email] = {
            'username': username,
            'password': password,
            'confirm_password': confirm_password
        }
        

        # Your frontend registration logic here
        
        return render_template('success.html', username=username, email=email, password=password, confirm_password=confirm_password)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
