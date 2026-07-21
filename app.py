from flask import Flask, render_template
from config import ADMIN_USERNAME, ADMIN_PASSWORD

app = Flask(__name__)


@app.route("/")
def home():
    return "PANNEL SHOP Admin Panel Running"


@app.route("/admin")
def admin():
    return f"""
    <h1>PANNEL SHOP ADMIN PANEL</h1>
    <p>Username: {ADMIN_USERNAME}</p>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
