# ✅ import from the 'project' package
from flask import Flask, render_template

app = Flask(__name__)

# --- Main site pages (HTML templates) ---
@app.route("/")
def home():
    return "Hello there"
    #return render_template('lobby.html')

@app.route("/contact")
def contact():
    return render_template('Contact.html')

@app.route('/farmers')
def farmers():
    return render_template('Farmers.html')

# --- Authentication ---
@app.route('/login')
def login():
    return render_template('LogIn.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/service')
def service():
    return render_template('service.html')

# --- Admin or test route ---
@app.route('/users')
def show_users():
    return render_template('users.html', users=["Hello World", "DankoPanko58", "Test User"])

@app.route('/Slovak/lobby')
def sk_lobby():
    return render_template('Slovak/lobby_sk.html')



if __name__ == '__main__':
    app.run()
