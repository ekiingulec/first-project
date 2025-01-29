from flask import Flask, request, jsonify, send_from_directory

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
    app.run(debug=True)
