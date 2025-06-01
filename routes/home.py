from flask import Blueprint, jsonify

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods=["GET"])
def home():
    """
    Displays a welcome message for the Football Data API.
    """
    return jsonify({"message": "Welcome to the Football Data API!"})