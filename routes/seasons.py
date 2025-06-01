from flask import Blueprint, jsonify, request
from models import Season
from databases import db  # Importa o objeto db

seasons_bp = Blueprint("seasons", __name__)

@seasons_bp.route("/seasons", methods=["GET"])
def get_seasons():
    """
    Returns a list of seasons.
    """
    seasons = Season.query.all()
    return jsonify([{"id": s.id, "name": s.name} for s in seasons])

@seasons_bp.route("/seasons", methods=["POST"])
def add_season():
    """
    Adds a new season to the database.
    """
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "Season name is required"}), 400

    if Season.query.filter_by(name=name).first():
        return jsonify({"error": "Season already exists"}), 400

    new_season = Season(name=name)
    db.session.add(new_season)
    db.session.commit()
    return jsonify({"message": f"Season '{name}' added successfully!"}), 201