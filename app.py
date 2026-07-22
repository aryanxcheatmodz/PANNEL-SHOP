from flask import Flask, request, session, redirect, url_for

from config import ADMIN_USERNAME, ADMIN_PASSWORD

app = Flask(__name__)
app.secret_key = "pannel_shop_secret"


@app.route("/")
def home():
    return """
    <h1>🔥 PANNEL SHOP</h1>
    <a href='/admin'>Admin Login</a><br>
    <a href='/user'>User Login</a>
    """


@app.route("/admin", methods=["GET","POST"])
def admin():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect("/dashboard")

        return "Wrong Login"

    return """
    <h2>Admin Login</h2>
    <form method="post">
    Username:<br>
    <input name="username"><br>
    Password:<br>
    <input name="password" type="password"><br><br>
    <button>Login</button>
    </form>
    """


@app.route("/dashboard")
def dashboard():

    if not session.get("admin"):
        return redirect("/admin")

    return """
    <h1>Admin Dashboard</h1>
    <p>✅ Login Successful</p>

    <a href="/generate">Generate Key</a>
    """


@app.route("/generate", methods=["GET","POST"])
def generate():

    if not session.get("admin"):
        return redirect("/admin")

    if request.method == "POST":
        username = request.form["username"]
        expire = request.form["expire"]

        return f"""
        <h2>Key Generated Successfully ✅</h2>
        <p>User: {username}</p>
        <p>Expire Date: {expire}</p>
        <p>Key: PANEL-{username}-2026</p>
        """

    return """
    <h2>Key Generate System</h2>

    <form method="post">
        <label>Enter Username:</label><br>
        <input type="text" name="username"><br><br>

        <label>Enter Expire Date:</label><br>
        <input type="date" name="expire"><br><br>

        <button type="submit">Generate Key</button>
    </form>
    """
@app.route("/user")
def user():

    return """
    <h2>User Login</h2>
    <p>User system coming next...</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
