from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🍔 Smart Canteen</h1>
    <p>Smart Canteen Flask website is working!</p>
    <a href="/login">Login</a>
    """

@app.route("/login")
def login():
    return """
    <h2>Smart Canteen Login</h2>
    <p>Login page is working!</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
    if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)