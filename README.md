# Health Information System

This is a simple Health Information System that allows doctors to:

- Create Health Programs (e.g., TB, Malaria, HIV)
- Register new Clients
- Enroll Clients into Health Programs
- Search for Clients by name
- View Client Profiles including enrolled programs
- Expose Client Profiles via an API

---

## 🛠 Tech Stack

- **Backend**: Flask, SQLAlchemy, SQLite
- **Frontend**: React, Axios
- **Database**: SQLite
- **Testing**: Pytest

---

## 🚀 Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/health_info_system.git
cd health_info_system

2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Backend will run at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

3. Frontend Setup
```bash
cd frontend
npm install
npm start
```

Frontend will run at: http://localhost:3000/

📚 API Endpoints
Method

Endpoint

Description

POST

/programs

Create a Health Program

POST

/clients

Register a new Client

POST

/enroll

Enroll a Client into one or more Programs

GET

/clients/search?name=<name>

Search Clients by name

GET

/clients/<client_id>

View Client Profile

GET

/programs/all

Fetch all Programs

🧪 Running Tests
```bash
cd backend
pytest test_app.py
```
