# backend/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, HealthProgram, Client

app = Flask(__name__)
CORS(app)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# ================= Routes ===================

@app.route('/programs', methods=['POST'])
def create_program():
    data = request.get_json()
    if not data.get('name'):
        return jsonify({'error': 'Program name is required'}), 400
    program = HealthProgram(name=data['name'])
    db.session.add(program)
    db.session.commit()
    return jsonify({'message': 'Health Program created successfully'}), 201

@app.route('/clients', methods=['POST'])
def register_client():
    data = request.get_json()
    if not data.get('name'):
        return jsonify({'error': 'Client name is required'}), 400
    client = Client(name=data['name'])
    db.session.add(client)
    db.session.commit()
    return jsonify({'message': 'Client registered successfully'}), 201

@app.route('/enroll', methods=['POST'])
def enroll_client():
    data = request.get_json()
    client_id = data.get('client_id')
    program_ids = data.get('program_ids')

    if not client_id or not program_ids:
        return jsonify({'error': 'Client ID and Program IDs are required'}), 400

    client = Client.query.get(client_id)
    if not client:
        return jsonify({'error': 'Client not found'}), 404

    programs = HealthProgram.query.filter(HealthProgram.id.in_(program_ids)).all()
    client.enrolled_programs.extend(programs)
    db.session.commit()
    return jsonify({'message': 'Client enrolled successfully'}), 200

@app.route('/clients/search', methods=['GET'])
def search_clients():
    name = request.args.get('name', '')
    clients = Client.query.filter(Client.name.ilike(f'%{name}%')).all()
    return jsonify([{'id': c.id, 'name': c.name} for c in clients])

@app.route('/clients/<int:client_id>', methods=['GET'])
def client_profile(client_id):
    client = Client.query.get_or_404(client_id)
    return jsonify({
        'id': client.id,
        'name': client.name,
        'programs': [program.name for program in client.enrolled_programs]
    })

@app.route('/programs/all', methods=['GET'])
def get_all_programs():
    programs = HealthProgram.query.all()
    return jsonify([{'id': p.id, 'name': p.name} for p in programs])


# Only run when direct
if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # Create tables
    app.run(debug=True)
# This code is a simple Flask application that provides an API for managing health programs and clients.
# It includes routes for creating health programs, registering clients, enrolling clients in programs,
# searching for clients, and retrieving client profiles. The application uses SQLAlchemy for database
# interactions and Flask-CORS for handling cross-origin requests. The database is configured to use SQLite
# and the tables are created when the application is run directly. The application runs in debug mode for
# development purposes.