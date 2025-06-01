from flask import Blueprint, jsonify, request
from models import League
from databases import db

leagues_bp = Blueprint("leagues", __name__)

@leagues_bp.route("/leagues", methods=["GET"])
def get_leagues():
    """
    Returns a list of leagues.
    """
    leagues = League.query.all()
    return jsonify([{"id": l.id, "name": l.name} for l in leagues])

@leagues_bp.route("/leagues", methods=["POST"])
def add_league():
    """
    Adds a new league to the database.
    """
    data = request.get_json()
    name = data.get("name")
    if not name:
        return jsonify({"error": "League name is required"}), 400

    if League.query.filter_by(name=name).first():
        return jsonify({"error": "League already exists"}), 400

    new_league = League(name=name)
    db.session.add(new_league)
    db.session.commit()
    return jsonify({"message": f"League '{name}' added successfully!"}), 201

@leagues_bp.route("/leagues/<int:id>", methods=["GET"])
def get_league_by_id(id):
    """
    Returns details of a specific league by ID.
    """
    league = League.query.get(id)
    if not league:
        return jsonify({"error": "League not found"}), 404
    return jsonify({"id": league.id, "name": league.name})

@leagues_bp.route("/leagues/<int:id>", methods=["DELETE"])
def delete_league(id):
    """
    Deletes a league by ID.
    """
    league = League.query.get(id)
    if not league:
        return jsonify({"error": "League not found"}), 404

    db.session.delete(league)
    db.session.commit()
    return jsonify({"message": f"League '{league.name}' deleted successfully!"}), 200