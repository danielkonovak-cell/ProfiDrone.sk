# ✅ import from the 'project' package
from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # --- Main site pages (HTML templates) ---
    @app.get('/')
    def home():
        return "Hello there"
        #return render_template('lobby.html')

    @app.get('/contact')
    def contact():
        return render_template('Contact.html') or "Site is too much to load"

    @app.get('/farmers')
    def farmers():
        return render_template('Farmers.html')

    # --- Authentication ---
    @app.get('/login')
    def login():
        return render_template('LogIn.html')

    @app.get('/register')
    def register():
        return render_template('register.html')
    
    @app.get('/service')
    def service():
        return render_template('service.html')

    # --- Admin or test get ---
    @app.get('/users')
    def show_users():
        return render_template('users.html', users=["Hello World", "DankoPanko58", "Test User"])
    
    @app.get('/Slovak/lobby')
    def sk_lobby():
        return render_template('Slovak/lobby_sk.html')
    return app


if __name__ == '__main__':
    create_app.run(debug=True)
