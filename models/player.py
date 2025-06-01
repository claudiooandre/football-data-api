from databases import db

class Player(db.Model):
    """
    Represents a football player.
    """
    __tablename__ = "players"
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the player
    name = db.Column(db.String(100), nullable=False)  # Name of the player
    position = db.Column(db.String(50), nullable=False)  # Position of the player (e.g., "Forward")
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"), nullable=False)  # ID of the team the player belongs to

    def __repr__(self):
        return f"<Player {self.name}>"