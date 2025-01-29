from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Basit kullanıcı verisi
users = {
    "admin": "password123",
    "testuser": "testpass"
}

@app.route("/")
def serve_frontend():
    return send_from_directory("static", "index.html")

@app.route("/home")
def serve_home():
    return send_from_directory("static", "home.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    if username in users and users[username] == password:
        return jsonify({"message": "Giriş başarılı!", "redirect": "\home"})
    else:
        return jsonify({"message": "Hatalı kullanıcı adı veya şifre!"}), 401

@app.route("/bet", methods=["POST"])
def place_bet():
    return jsonify({"message": "Bahis başarıyla yapıldı!"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render'ın atadığı portu al
    app.run(host="0.0.0.0", port=port, debug=False)
