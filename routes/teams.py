from flask import Blueprint, jsonify, request
from models import Team

teams_bp = Blueprint("teams", __name__)

@teams_bp.route("/teams", methods=["GET"])
def get_teams():
    """
    Returns a paginated list of teams. Optionally filters by season if a query parameter is provided.
    """
    season = request.args.get("season")  # Get the season filter from query parameters
    page = request.args.get("page", 1, type=int)  # Current page (default: 1)
    per_page = request.args.get("per_page", 10, type=int)  # Records per page (default: 10)

    query = Team.query
    if season:
        query = query.filter_by(season=season)

    paginated_teams = query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "total": paginated_teams.total,
        "pages": paginated_teams.pages,
        "current_page": paginated_teams.page,
        "per_page": paginated_teams.per_page,
        "teams": [
            {"id": t.id, "team": t.team, "country": t.country, "season": t.season}
            for t in paginated_teams.items
        ]
    })

@teams_bp.route("/teams/<int:id>", methods=["GET"])
def get_team_by_id(id):
    """
    Returns details of a specific team by ID.
    """
    team = Team.query.get(id)
    if not team:
        return jsonify({"error": "Team not found"}), 404
    return jsonify({"id": team.id, "team": team.team, "country": team.country, "season": team.season})