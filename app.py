from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart Canteen</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: #f2f2f2;
                padding-top: 80px;
            }

            .box {
                background: white;
                width: 350px;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px #ccc;
            }

            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
        </style>
    </head>

    <body>
        <div class="box">
            <h1>🍔 Smart Canteen</h1>
            <p>Welcome to Smart Canteen</p>

            <a href="/login">Login</a>
        </div>
    </body>
    </html>
    """


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if email == "admin@canteen.com" and password == "admin123":
            return """
            <h1>Welcome Admin! 👨‍💼</h1>
            <p>Login successful.</p>
            <a href="/">Back to Home</a>
            """

        elif email == "student@gmail.com" and password == "student123":
            return """
            <h1>Welcome Student! 👨‍🎓</h1>
            <p>Login successful.</p>
            <a href="/">Back to Home</a>
            """

        else:
            return """
            <h2>❌ Invalid Login</h2>
            <p>Incorrect email or password.</p>
            <a href="/login">Try Again</a>
            """

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart Canteen Login</title>

        <style>
            body {
                font-family: Arial;
                background: #f2f2f2;
                text-align: center;
                padding-top: 70px;
            }

            .login-box {
                background: white;
                width: 350px;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px #ccc;
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

            button:hover {
                background: #218838;
            }

            a {
                display: inline-block;
                margin-top: 20px;
            }
        </style>
    </head>

    <body>

        <div class="login-box">

            <h1>🍔 Smart Canteen</h1>
            <h2>Login</h2>

            <form method="POST">

                <input
                    type="email"
                    name="email"
                    placeholder="Enter Email"
                    required
                >

                <input
                    type="password"
                    name="password"
                    placeholder="Enter Password"
                    required
                >

                <button type="submit">Login</button>

            </form>

            <a href="/">Back to Home</a>

        </div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)