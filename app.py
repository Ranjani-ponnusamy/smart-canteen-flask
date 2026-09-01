from flask import Flask, redirect, url_for, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login")
def login():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart Canteen - Login</title>
        <style>
            body {
                font-family: Arial;
                background: #f2f2f2;
                text-align: center;
                padding-top: 100px;
            }

            .login-box {
                background: white;
                width: 350px;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px #aaa;
            }

            input {
                width: 90%;
                padding: 12px;
                margin: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            button {
                width: 95%;
                padding: 12px;
                background: #28a745;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }

            h1 {
                color: #333;
            }
        </style>
    </head>

    <body>

        <div class="login-box">

            <h1>🍔 Smart Canteen</h1>

            <h2>Login</h2>

            <form>
                <input type="email" placeholder="Enter Email" required>

                <input type="password" placeholder="Enter Password" required>

                <button type="submit">Login</button>
            </form>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)