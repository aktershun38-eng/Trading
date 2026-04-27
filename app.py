from flask import Flask, request, jsonify
import bcrypt

app = Flask(__name__)

users = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']

    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    users[username] = hashed

    return jsonify({"message": "User registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    if username in users:
        if bcrypt.checkpw(password.encode('utf-8'), users[username]):
            return jsonify({"message": "Login successful"})
    
    return jsonify({"message": "Invalid credentials"})

if __name__ == '__main__':
    app.run(debug=True)
