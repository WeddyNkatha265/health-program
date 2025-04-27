# Go into backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

# Install Flask and libraries
pip install flask flask_sqlalchemy flask_cors

# Save dependencies
pip freeze > requirements.txt

# Run backend server
flask run

By default, Flask will run on: http://127.0.0.1:5000

# Health Information System Backend

## Tech Stack
- Flask (Python)
- SQLite
- SQLAlchemy
- Flask-CORS

## How to Run

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
