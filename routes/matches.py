from flask import Blueprint, jsonify, request
from models import Match
from databases import db 

matches_bp = Blueprint("matches", __name__)

@matches_bp.route("/matches", methods=["GET"])
def get_matches():
    """
    Returns a paginated list of matches. Optionally filters by season if a query parameter is provided.
    """
    season = request.args.get("season")
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 10, type=int)

    query = Match.query
    if season:
        query = query.filter_by(season=season)

    paginated_matches = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "total": paginated_matches.total,
        "pages": paginated_matches.pages,
        "current_page": paginated_matches.page,
        "per_page": paginated_matches.per_page,
        "matches": [
            {
                "id": m.id,
                "team1": m.team1,
                "team2": m.team2,
                "score": m.score,
                "season": m.season,
                "league": m.league
            }
            for m in paginated_matches.items
        ]
    })

@matches_bp.route("/matches/<int:id>", methods=["GET"])
def get_match_by_id(id):
    """
    Returns details of a specific match by ID.
    """
    match = Match.query.get(id)
    if not match:
        return jsonify({"error": "Match not found"}), 404
    return jsonify({
        "id": match.id,
        "team1": match.team1,
        "team2": match.team2,
        "score": match.score,
        "season": match.season,
        "league": match.league
    })

@matches_bp.route("/matches", methods=["POST"])
def add_match():
    """
    Adds a new match to the database.
    """
    data = request.get_json()  # Parse the JSON body of the request

    # Extract match details from the request
    team1 = data.get("team1")
    team2 = data.get("team2")
    score = data.get("score")
    season = data.get("season")
    league = data.get("league")

    # Ensure all required fields are provided
    if not all([team1, team2, score, season, league]):
        return jsonify({"error": "All fields are required"}), 400

    # Check if the league exists
    from models import League  # Import League model
    league_exists = League.query.filter_by(name=league).first()
    if not league_exists:
        return jsonify({"error": f"League '{league}' does not exist"}), 400

    # Create and save the match
    new_match = Match(team1=team1, team2=team2, score=score, season=season, league=league)
    db.session.add(new_match)
    db.session.commit()
    return jsonify({"message": "Match added successfully!"}), 201