from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        
        # You can process the user data here, e.g., store it in a database
        return render_template('success.html', username=username, email=email, password=password, confirm_password=confirm_password)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
