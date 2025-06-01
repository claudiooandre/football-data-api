from databases import db

class Season(db.Model):
    """
    Represents a football season.
    """
    __tablename__ = "seasons"
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the season
    name = db.Column(db.String(50), unique=True, nullable=False)  # Name of the season (e.g., "2024/2025")

    def __repr__(self):
        return f"<Season {self.name}>"