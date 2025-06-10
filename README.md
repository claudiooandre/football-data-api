# Football Data API Backend

A Python backend API for managing and querying football statistics data, including leagues, teams, players, seasons, and matches.

## Project Structure

```
.
├── App.py
├── Requirements.txt
├── README.md
├── databases
│   └── database.db
├── Models
│   ├── league.py
│   ├── match.py
│   ├── player.py
│   ├── season.py
│   └── team.py
├── Routes
│   ├── home.py
│   ├── leagues.py
│   ├── matches.py
│   ├── seasons.py
│   └── teams.py
└── Scripts
    ├── add_player.py
    ├── add_teams.py
    └── reset_teams.py
```

## Features

- Full CRUD operations for teams, players, seasons, matches, and leagues
- SQLite database (`database.db`)
- Modular architecture using FastAPI or Flask
- Utility scripts for managing and resetting data

## Technologies Used

- Python 3.x
- FastAPI *(or Flask, depending on your setup)*
- SQLite
- SQLAlchemy *(or another ORM if used)*

## Getting Started

1. **Clone the repository**:
```bash
git clone https://gitlab.com/claudio-rodrigues1/football-data-api.git
cd football-data-api
```

2. **Create and activate a virtual environment** (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r Requirements.txt
```

4. **Run the application**:
```bash
python App.py
```

## API Endpoints

- `GET /` – Home route
- `GET /teams` – Retrieve all teams
- `POST /teams` – Add a new team
- `GET /players` – Retrieve all players
- `POST /players` – Add a new player
- `GET /leagues` – Retrieve leagues
- `GET /matches` – Retrieve match data
- `GET /seasons` – Retrieve seasons

*(Document more routes as needed based on your implementation)*

## Utility Scripts

- `add_player.py`: Add new players to the database
- `add_teams.py`: Add teams to the database
- `reset_teams.py`: Reset all team data
