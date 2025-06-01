from databases import db

class League(db.Model):
    """
    Represents a football league.
    """
    __tablename__ = "leagues"
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the league
    name = db.Column(db.String(100), unique=True, nullable=False)  # Name of the league (e.g., "Premier League")

    def __repr__(self):
        return f"<League {self.name}>"