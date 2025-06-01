from flask import Blueprint
from routes.home import home_bp
from routes.teams import teams_bp
from routes.matches import matches_bp
from routes.seasons import seasons_bp
from routes.leagues import leagues_bp

def register_routes(app):
    """
    Register all routes (blueprints) with the Flask app.
    """
    app.register_blueprint(home_bp)
    app.register_blueprint(teams_bp)
    app.register_blueprint(matches_bp)
    app.register_blueprint(seasons_bp)
    app.register_blueprint(leagues_bp)