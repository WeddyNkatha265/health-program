import pytest
from app import app, db, HealthProgram, Client

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory DB for tests
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_create_program(client):
    response = client.post('/programs', json={'name': 'Malaria Program'})
    assert response.status_code == 201
    assert b'Health Program created successfully' in response.data

def test_register_client(client):
    response = client.post('/clients', json={'name': 'John Doe'})
    assert response.status_code == 201
    assert b'Client registered successfully' in response.data

def test_enroll_client(client):
    # First create program
    client.post('/programs', json={'name': 'TB Program'})
    # Then register client
    client.post('/clients', json={'name': 'Jane Doe'})

    # Fetch program and client IDs
    programs = client.get('/programs/all').get_json()
    program_id = programs[0]['id']

    clients = client.get('/clients/search?name=Jane').get_json()
    client_id = clients[0]['id']

    # Enroll
    response = client.post('/enroll', json={
        'client_id': client_id,
        'program_ids': [program_id]
    })
    assert response.status_code == 200
    assert b'Client enrolled in programs' in response.data

def test_client_profile(client):
    # Setup
    client.post('/programs', json={'name': 'HIV Program'})
    client.post('/clients', json={'name': 'Mark Doe'})
    programs = client.get('/programs/all').get_json()
    program_id = programs[0]['id']
    clients = client.get('/clients/search?name=Mark').get_json()
    client_id = clients[0]['id']
    client.post('/enroll', json={'client_id': client_id, 'program_ids': [program_id]})

    # Test profile
    res = client.get(f'/clients/{client_id}')
    profile = res.get_json()

    assert res.status_code == 200
    assert profile['name'] == 'Mark Doe'
    assert 'HIV Program' in profile['programs']
