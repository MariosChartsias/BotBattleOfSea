from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/process', methods=['POST'])
def process():
    data = request.json
    # Process the data received from the external system
    # For example, you can validate the data, store it in a database, etc.
    # Then return a response
    if all(key in data for key in ['username', 'email', 'password', 'confirm_password']):
        # Example processing
        username = data['username']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']
        
        # Do whatever processing you need here
        
        return jsonify({"message": "Data processed successfully"})
    else:
        return jsonify({"error": "Incomplete data received"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=8080)
