import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db
from models import Team

def reset_teams():
    """
    Resets the teams table by deleting all existing teams.
    """
    with app.app_context():
        # Deleta todas as equipes
        db.session.query(Team).delete()
        db.session.commit()
        print("All teams have been deleted.")

if __name__ == "__main__":
    reset_teams()