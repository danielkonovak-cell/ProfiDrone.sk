from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv
import urllib.parse  # ✅ needed for password encoding

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Load environment variables
    mysql_user = os.getenv('MYSQL_USER', 'root')
    mysql_password = os.getenv('MYSQL_PASSWORD', '')
    mysql_host = os.getenv('MYSQL_HOST', '127.0.0.1')
    mysql_port = os.getenv('MYSQL_PORT', '3306')
    mysql_db = os.getenv('MYSQL_DB', 'why')

    # ✅ Encode password for special characters (like '@')
    encoded_password = urllib.parse.quote_plus(mysql_password)

    # ✅ Build the connection string
    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+mysqlconnector://{mysql_user}:{encoded_password}@{mysql_host}:{mysql_port}/{mysql_db}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)

    # ✅ REGISTER YOUR BLUEPRINT HERE
    # ---------------------------------------------------
    from .routes import views      # 👈 import your Blueprint
    app.register_blueprint(views)  # 👈 register it with Flask
    # ---------------------------------------------------

    print("✅ Flask app configured and database connected URI:")
    print(app.config['SQLALCHEMY_DATABASE_URI'])

    return app
