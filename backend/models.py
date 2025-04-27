# backend/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Association table
enrollments = db.Table('enrollments',
    db.Column('client_id', db.Integer, db.ForeignKey('client.id'), primary_key=True),
    db.Column('program_id', db.Integer, db.ForeignKey('health_program.id'), primary_key=True)
)

class HealthProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    enrolled_programs = db.relationship('HealthProgram', secondary=enrollments, backref='clients')
