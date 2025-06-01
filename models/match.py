from databases import db

class Match(db.Model):
    """
    Represents a football match between two teams.
    """
    __tablename__ = "matches"
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the match
    team1 = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)  # ID of the first team
    team2 = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)  # ID of the second team
    score = db.Column(db.String(10), nullable=False)  # Match score (e.g., "2-1")
    season = db.Column(db.String(50), nullable=False)  # Season the match belongs to
    league = db.Column(db.String(100), nullable=False)  # League the match belongs to

    def __repr__(self):
        return f"<Match {self.team1} vs {self.team2}>"