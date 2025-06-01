from databases import db

class Team(db.Model):
    """
    Represents a football team.
    """
    __tablename__ = "teams"
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the team
    team = db.Column(db.String(100), nullable=False)  # Name of the team
    country = db.Column(db.String(100), nullable=False)  # Country of the team
    season = db.Column(db.String(50), nullable=False)  # Season the team belongs to

    # Relationship to the Player model
    players = db.relationship("Player", backref="team", lazy=True)

    def __repr__(self):
        return f"<Team {self.team}>"