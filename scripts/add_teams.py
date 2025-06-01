import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, db
from models import Team

def add_teams():
    """
    Adds teams to the database.
    """
    with app.app_context():
        # Define the teams to add
        teams = [
            {"team": "Arsenal", "country": "England", "season": "2024/2025"},
            {"team": "Manchester City", "country": "England", "season": "2024/2025"},
            {"team": "Liverpool", "country": "England", "season": "2024/2025"},
            {"team": "Chelsea", "country": "England", "season": "2024/2025"},
            {"team": "Tottenham Hotspur", "country": "England", "season": "2024/2025"},
            {"team": "Manchester United", "country": "England", "season": "2024/2025"},
            {"team": "Newcastle United", "country": "England", "season": "2024/2025"},
            {"team": "Aston Villa", "country": "England", "season": "2024/2025"},
            {"team": "Brighton & Hove Albion", "country": "England", "season": "2024/2025"},
            {"team": "West Ham United", "country": "England", "season": "2024/2025"},
            {"team": "Wolverhampton Wanderers", "country": "England", "season": "2024/2025"},
            {"team": "Crystal Palace", "country": "England", "season": "2024/2025"},
            {"team": "Fulham", "country": "England", "season": "2024/2025"},
            {"team": "Brentford", "country": "England", "season": "2024/2025"},
            {"team": "Everton", "country": "England", "season": "2024/2025"},
            {"team": "Nottingham Forest", "country": "England", "season": "2024/2025"},
            {"team": "Bournemouth", "country": "England", "season": "2024/2025"},
            {"team": "Burnley", "country": "England", "season": "2024/2025"},
            {"team": "Sheffield United", "country": "England", "season": "2024/2025"},
            {"team": "Luton Town", "country": "England", "season": "2024/2025"}
        ]

        # Add each team to the database
        for team_data in teams:
            # Check if the team already exists
            existing_team = Team.query.filter_by(team=team_data["team"], season=team_data["season"]).first()
            if not existing_team:
                new_team = Team(
                    team=team_data["team"],
                    country=team_data["country"],
                    season=team_data["season"]
                )
                db.session.add(new_team)
                print(f"Added team: {team_data['team']} ({team_data['country']})")
            else:
                print(f"Team already exists: {team_data['team']} ({team_data['season']})")

        # Commit changes
        db.session.commit()
        print("Teams added successfully!")

if __name__ == "__main__":
    add_teams()