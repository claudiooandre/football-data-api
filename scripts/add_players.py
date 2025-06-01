from app import app, db
from models import Player, Team

def add_players():
    """
    Adds players to teams in the database.
    """
    with app.app_context():
        # Find teams
        arsenal = Team.query.filter_by(team="Arsenal").first()
        barcelona = Team.query.filter_by(team="Barcelona").first()

        # Add players to Arsenal
        if arsenal:
            player1 = Player(name="Bukayo Saka", position="Forward", team_id=arsenal.id)
            player2 = Player(name="Martin Ødegaard", position="Midfielder", team_id=arsenal.id)
            db.session.add_all([player1, player2])

        # Add players to Barcelona
        if barcelona:
            player3 = Player(name="Robert Lewandowski", position="Forward", team_id=barcelona.id)
            player4 = Player(name="Pedri", position="Midfielder", team_id=barcelona.id)
            db.session.add_all([player3, player4])

        # Commit changes
        db.session.commit()
        print("Players added successfully!")

if __name__ == "__main__":
    add_players()