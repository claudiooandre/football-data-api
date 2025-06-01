from flask import Flask, jsonify
from flask_cors import CORS
from databases import db
from models import Team, Match, Season, League, Player
from routes import register_routes
import os

# Initialize the Flask app
app = Flask(__name__)
CORS(app)

# Configure SQLite database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_DIR = os.path.join(BASE_DIR, "databases")
os.makedirs(DATABASE_DIR, exist_ok=True)
DATABASE_PATH = os.path.join(DATABASE_DIR, "database.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DATABASE_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize SQLAlchemy
db.init_app(app)

# Create the database tables if they don't exist
with app.app_context():
    db.create_all()

# Register routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)