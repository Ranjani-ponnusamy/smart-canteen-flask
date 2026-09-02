from flask import Flask, request, redirect, session

app = Flask(__name__)
app.secret_key = "smart-canteen-secret"


# ---------------- HOME ----------------

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Smart Canteen</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f4f4;
                text-align: center;
                margin: 0;
            }

            header {
                background: #333;
                color: white;
                padding: 25px;
            }

            .container {
                background: white;
                width: 80%;
                max-width: 700px;
                margin: 40px auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 10px #ccc;
            }

            a, button {
                display: inline-block;
                padding: 12px 20px;
                margin: 8px;
                background: #333;
                color: white;
                text-decoration: none;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>🍔 Smart Canteen</h1>
            <p>Student Pre-Order System</p>
        </header>

        <div class="container">

            <h2>Welcome to Smart Canteen</h2>

            <p>Order your favourite food easily!</p>

            <a href="/login">🔐 Login</a>

        </div>

    </body>
    </html>
    """


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if email == "admin@canteen.com" and password == "admin123":

            session["role"] = "admin"
            session["name"] = "Admin"

            return redirect("/admin/dashboard")

        elif email == "teststudent@gmail.com" and password == "student123":

            session["role"] = "student"
            session["name"] = "Ranjani"

            return redirect("/student/dashboard")

        else:

            return """
            <h2>❌ Invalid Login</h2>
            <p>Incorrect email or password.</p>
            <a href="/login">Try Again</a>
            """

    return """
    <html>
    <head>
        <title>Login - Smart Canteen</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f4f4;
                text-align: center;
            }

            .box {
                background: white;
                width: 350px;
                margin: 80px auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 10px #ccc;
            }

            input {
                width: 90%;
                padding: 12px;
                margin: 10px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }

            button {
                padding: 12px 30px;
                background: #333;
                color: white;
                border: none;
                border-radius: 7px;
                cursor: pointer;
            }

            a {
                display: block;
                margin: 20px;
            }
        </style>
    </head>

    <body>

        <div class="box">

            <h1>🍔 Smart Canteen</h1>

            <h2>🔐 Login</h2>

            <form method="POST">

                <input type="email"
                       name="email"
                       placeholder="Enter Email"
                       required>

                <input type="password"
                       name="password"
                       placeholder="Enter Password"
                       required>

                <br>

                <button type="submit">Login</button>

            </form>

            <a href="/">⬅ Back to Home</a>

        </div>

    </body>
    </html>
    """


# ---------------- STUDENT DASHBOARD ----------------

@app.route("/student/dashboard")
def student_dashboard():

    return """
    <html>
    <head>
        <title>Student Dashboard</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f4f4;
                text-align: center;
                margin: 0;
            }

            header {
                background: #333;
                color: white;
                padding: 25px;
            }

            .container {
                background: white;
                width: 80%;
                max-width: 700px;
                margin: 40px auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 10px #ccc;
            }

            .menu a {
                display: block;
                padding: 15px;
                margin: 12px;
                background: #333;
                color: white;
                text-decoration: none;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>🍔 Smart Canteen</h1>
            <p>Student Dashboard 👨‍🎓</p>
        </header>

        <div class="container">

            <h2>Welcome, Ranjani! 👋</h2>

            <div class="menu">

                <a href="/student/food">
                    🍔 Food Menu
                </a>

                <a href="/student/cart">
                    🛒 Cart
                </a>

                <a href="/student/bill">
                    🧾 Bill
                </a>

                <a href="/student/orders">
                    📦 My Orders
                </a>

                <a href="/logout">
                    🚪 Logout
                </a>

            </div>

        </div>

    </body>
    </html>
    """


# ---------------- FOOD MENU ----------------

@app.route("/student/food")
def student_food():

    return """
    <html>
    <head>
        <title>Food Menu</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f4f4;
                text-align: center;
            }

            .food {
                background: white;
                width: 250px;
                margin: 30px auto;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 0 10px #ccc;
            }

            button, a {
                padding: 10px 20px;
                margin: 8px;
                background: #333;
                color: white;
                border: none;
                border-radius: 7px;
                text-decoration: none;
            }
        </style>
    </head>

    <body>

        <h1>🍔 Food Menu</h1>

        <div class="food">

            <h2>🍔 Burger</h2>
            <p>Price: ₹80</p>

            <a href="/student/add/burger">Add to Cart</a>

        </div>

        <div class="food">

            <h2>🍕 Pizza</h2>
            <p>Price: ₹120</p>

            <a href="/student/add/pizza">Add to Cart</a>

        </div>

        <div class="food">

            <h2>🥪 Sandwich</h2>
            <p>Price: ₹60</p>

            <a href="/student/add/sandwich">Add to Cart</a>

        </div>

        <a href="/student/dashboard">⬅ Dashboard</a>

    </body>
    </html>
    """


# ---------------- ADD TO CART ----------------

@app.route("/student/add/<item>")
def add_to_cart(item):

    prices = {
        "burger": 80,
        "pizza": 120,
        "sandwich": 60
    }

    names = {
        "burger": "Burger",
        "pizza": "Pizza",
        "sandwich": "Sandwich"
    }

    if item in prices:

        if "cart" not in session:
            session["cart"] = []

        session["cart"].append({
            "name": names[item],
            "price": prices[item]
        })

        session.modified = True

    return redirect("/student/cart")


# ---------------- CART ----------------

@app.route("/student/cart")
def student_cart():

    cart = session.get("cart", [])

    total = sum(item["price"] for item in cart)

    items = ""

    for item in cart:

        items += f"""
        <p>
            {item["name"]} - ₹{item["price"]}
        </p>
        """

    if not items:
        items = "<p>Cart is empty.</p>"

    return f"""
    <html>
    <head>
        <title>Cart</title>
        <style>
            body {{
                font-family: Arial;
                background: #f4f4f4;
                text-align: center;
            }}

            .box {{
                background: white;
                width: 500px;
                margin: 50px auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 10px #ccc;
            }}

            a {{
                display: inline-block;
                padding: 12px 20px;
                margin: 10px;
                background: #333;
                color: white;
                text-decoration: none;
                border-radius: 7px;
            }}
        </style>
    </head>

    <body>

        <div class="box">

            <h1>🛒 Your Cart</h1>

            {items}

            <hr>

            <h2>Total: ₹{total}</h2>

            <a href="/student/food">🍔 Add More</a>

            <a href="/student/place-order">📦 Place Order</a>

            <a href="/student/dashboard">⬅ Dashboard</a>

        </div>

    </body>
    </html>
    """


# ---------------- PLACE ORDER ----------------

@app.route("/student/place-order")
def place_order():

    cart = session.get("cart", [])

    if not cart:
        return redirect("/student/cart")

    total = sum(item["price"] for item in cart)

    session["last_order"] = {
        "items": cart,
        "total": total,
        "status": "Pending"
    }

    session["cart"] = []

    return redirect("/student/bill")


# ---------------- BILL ----------------

@app.route("/student/bill")
def student_bill():

    order = session.get("last_order")

    if not order:
        return """
        <h2>No order found.</h2>
        <a href="/student/food">Food Menu</a>
        """

    items = ""

    for item in order["items"]:

        items += f"""
        <tr>
            <td>{item["name"]}</td>
            <td>₹{item["price"]}</td>
        </tr>
        """

    return f"""
    <html>
    <head>
        <title>Bill - Smart Canteen</title>

        <style>
            body {{
                font-family: Arial;
                background: #f4f4f4;
                text-align: center;
            }}

            .bill {{
                background: white;
                width: 500px;
                margin: 40px auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 10px #ccc;
            }}

            table {{
                width: 100%;
                border-collapse: collapse;
            }}

            td, th {{
                padding: 12px;
                border-bottom: 1px solid #ddd;
            }}

            a {{
                display: inline-block;
                padding: 12px 20px;
                margin: 10px;
                background: #333;
                color: white;
                text-decoration: none;
                border-radius: 7px;
            }}
        </style>
    </head>

    <body>

        <div class="bill">

            <h1>🍔 Smart Canteen</h1>

            <h2>🧾 Order Bill</h2>

            <p><b>Student:</b> Ranjani</p>

            <p><b>Status:</b> {order["status"]}</p>

            <hr>

            <table>

                <tr>
                    <th>Food</th>
                    <th>Price</th>
                </tr>

                {items}

            </table>

            <h2>Total: ₹{order["total"]}</h2>

            <a href="/student/orders">📦 My Orders</a>

            <a href="/student/dashboard">⬅ Dashboard</a>

        </div>

    </body>
    </html>
    """


# ---------------- MY ORDERS ----------------

@app.route("/student/orders")
def student_orders():

    order = session.get("last_order")

    if not order:

        order_text = "<p>No orders yet.</p>"

    else:

        order_text = f"""
        <h3>Order #001</h3>

        <p>Total Amount: ₹{order["total"]}</p>

        <p>Status: <b>{order["status"]}</b></p>

        <a href="/student/bill">🧾 View Bill</a>
        """

    return f"""
    <html>
    <head>
        <title>My Orders</title>
        <style>
            body {{
                font-family: Arial;
                background: #f4f4f4;
                text-align: center;
            }}

            .box {{
                background: white;
                width: 500px;
                margin: 50px auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 10px #ccc;
            }}

            a {{
                display: inline-block;
                padding: 12px 20px;
                margin: 10px;
                background: #333;
                color: white;
                text-decoration: none;
                border-radius: 7px;
            }}
        </style>
    </head>

    <body>

        <div class="box">

            <h1>📦 My Orders</h1>

            {order_text}

            <a href="/student/dashboard">⬅ Dashboard</a>

        </div>

    </body>
    </html>
    """


# ---------------- ADMIN DASHBOARD ----------------

@app.route("/admin/dashboard")
def admin_dashboard():

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Admin Dashboard - Smart Canteen</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                margin: 0;
            }

            header {
                background: #333;
                color: white;
                padding: 25px;
                text-align: center;
            }

            .container {
                width: 90%;
                max-width: 1000px;
                margin: 40px auto;
            }

            .welcome {
                text-align: center;
                margin-bottom: 30px;
            }

            .cards {
                display: flex;
                justify-content: center;
                gap: 25px;
                flex-wrap: wrap;
            }

            .card {
                background: white;
                width: 240px;
                padding: 30px 20px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 0 10px #ccc;
            }

            .card h2 {
                margin-bottom: 10px;
            }

            .card p {
                color: #666;
                min-height: 45px;
            }

            .button {
                display: inline-block;
                padding: 12px 22px;
                margin-top: 15px;
                background: #333;
                color: white;
                text-decoration: none;
                border-radius: 8px;
            }

            .button:hover {
                background: #555;
            }

            .logout {
                display: block;
                width: 150px;
                margin: 40px auto;
                padding: 12px;
                background: #c62828;
                color: white;
                text-decoration: none;
                text-align: center;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>🍔 Smart Canteen</h1>
            <p>Admin Panel</p>
        </header>

        <div class="container">

            <div class="welcome">
                <h2>👨‍💼 Admin Dashboard</h2>
                <p>Welcome, Admin!</p>
            </div>

            <div class="cards">

                <div class="card">
                    <h2>🍔</h2>
                    <h3>Manage Food</h3>
                    <p>Add and view available food items.</p>

                    <a class="button" href="/admin/foods">
                        Open
                    </a>
                </div>

                <div class="card">
                    <h2>📦</h2>
                    <h3>Orders</h3>
                    <p>View student food orders and status.</p>

                    <a class="button" href="/admin/orders">
                        Open
                    </a>
                </div>

                <div class="card">
                    <h2>👥</h2>
                    <h3>Students</h3>
                    <p>View registered student information.</p>

                    <a class="button" href="/admin/students">
                        Open
                    </a>
                </div>

            </div>

            <a class="logout" href="/logout">
                🚪 Logout
            </a>

        </div>

    </body>
    </html>
    """


# ---------------- ADMIN FOOD ----------------

@app.route("/admin/foods")
def admin_foods():

    return """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Manage Food - Smart Canteen</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                margin: 0;
            }

            header {
                background: #333;
                color: white;
                padding: 25px;
                text-align: center;
            }

            .container {
                width: 90%;
                max-width: 1000px;
                margin: 40px auto;
            }

            h2 {
                text-align: center;
            }

            .foods {
                display: flex;
                justify-content: center;
                gap: 25px;
                flex-wrap: wrap;
            }

            .food {
                background: white;
                width: 220px;
                padding: 25px;
                text-align: center;
                border-radius: 15px;
                box-shadow: 0 0 10px #ccc;
            }

            .food h3 {
                font-size: 22px;
            }

            .price {
                font-size: 20px;
                font-weight: bold;
            }

            .available {
                color: green;
                font-weight: bold;
            }

            .back {
                display: block;
                width: 220px;
                margin: 35px auto;
                padding: 12px;
                background: #333;
                color: white;
                text-decoration: none;
                text-align: center;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>🍔 Smart Canteen</h1>
            <p>Food Management</p>
        </header>

        <div class="container">

            <h2>🍔 Manage Food Items</h2>

            <div class="foods">

                <div class="food">
                    <h3>🍔 Burger</h3>
                    <p class="price">₹80</p>
                    <p class="available">✓ Available</p>
                </div>

                <div class="food">
                    <h3>🍕 Pizza</h3>
                    <p class="price">₹120</p>
                    <p class="available">✓ Available</p>
                </div>

                <div class="food">
                    <h3>🥪 Sandwich</h3>
                    <p class="price">₹60</p>
                    <p class="available">✓ Available</p>
                </div>

            </div>

            <a class="back" href="/admin/dashboard">
                ⬅ Back to Dashboard
            </a>

        </div>

    </body>
    </html>
    """


# ---------------- ADMIN ORDERS ----------------

@app.route("/admin/orders")
def admin_orders():

    return """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Orders - Smart Canteen</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                margin: 0;
            }

            header {
                background: #333;
                color: white;
                padding: 25px;
                text-align: center;
            }

            .container {
                width: 90%;
                max-width: 1000px;
                margin: 40px auto;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 10px #ccc;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 25px;
            }

            th, td {
                padding: 15px;
                border-bottom: 1px solid #ddd;
                text-align: center;
            }

            th {
                background: #333;
                color: white;
            }

            .pending {
                color: orange;
                font-weight: bold;
            }

            .back {
                display: block;
                width: 220px;
                margin: 30px auto 0;
                padding: 12px;
                background: #333;
                color: white;
                text-decoration: none;
                text-align: center;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>🍔 Smart Canteen</h1>
            <p>Order Management</p>
        </header>

        <div class="container">

            <h2>📦 Student Orders</h2>

            <table>

                <tr>
                    <th>Order ID</th>
                    <th>Student</th>
                    <th>Food</th>
                    <th>Amount</th>
                    <th>Status</th>
                </tr>

                <tr>
                    <td>#001</td>
                    <td>Ranjani</td>
                    <td>Burger</td>
                    <td>₹80</td>
                    <td class="pending">Pending</td>
                </tr>

            </table>

            <a class="back" href="/admin/dashboard">
                ⬅ Back to Dashboard
            </a>

        </div>

    </body>
    </html>
    """


# ---------------- ADMIN STUDENTS ----------------

@app.route("/admin/students")
def admin_students():

    return """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Students - Smart Canteen</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f4;
                margin: 0;
            }

            header {
                background: #333;
                color: white;
                padding: 25px;
                text-align: center;
            }

            .container {
                width: 90%;
                max-width: 800px;
                margin: 40px auto;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 10px #ccc;
            }

            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 25px;
            }

            th, td {
                padding: 15px;
                border-bottom: 1px solid #ddd;
                text-align: center;
            }

            th {
                background: #333;
                color: white;
            }

            .back {
                display: block;
                width: 220px;
                margin: 30px auto 0;
                padding: 12px;
                background: #333;
                color: white;
                text-decoration: none;
                text-align: center;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>🍔 Smart Canteen</h1>
            <p>Student Management</p>
        </header>

        <div class="container">

            <h2 style="text-align:center;">
                👥 Registered Students
            </h2>

            <table>

                <tr>
                    <th>Name</th>
                    <th>Email</th>
                </tr>

                <tr>
                    <td>Ranjani</td>
                    <td>teststudent@gmail.com</td>
                </tr>

            </table>

            <a class="back" href="/admin/dashboard">
                ⬅ Back to Dashboard
            </a>

        </div>

    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)