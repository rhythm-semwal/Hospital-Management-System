
from app import db
from sqlalchemy import JSON


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    contact_info = db.Column(db.String(100))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))

    # Relationships
    medical_history = db.relationship('MedicalHistory', backref='patient', lazy=True)
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'contact_info': self.contact_info,
            'doctor_id': self.doctor_id,  # Include doctor_id in serialization
            'medical_history': [history.serialize() for history in self.medical_history],
            'appointments': [appointment.serialize() for appointment in self.appointments]
        }


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    contact_info = db.Column(db.String(100))
    availability_schedule = db.Column(JSON)

    appointments = db.relationship('Appointment', backref='doctor', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'specialization': self.specialization,
            'contact_info': self.contact_info,
            'availability_schedule': self.availability_schedule
        }


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    services_offered = db.Column(db.String(255))

    # Relationships
    doctors = db.relationship('Doctor', backref='department', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'services_offered': self.services_offered,
            'doctors': [doctor.serialize() for doctor in self.doctors]
        }


class MedicalHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    diagnosis = db.Column(db.String(255))
    allergies = db.Column(db.String(255))
    medications = db.Column(db.String(255))

    patient = db.relationship('Patient', backref=db.backref('medical_history', cascade='all, delete-orphan'))

    def serialize(self):
        return {
            'id': self.id,
            'diagnosis': self.diagnosis,
            'allergies': self.allergies,
            'medications': self.medications,
        }


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    appointment_date = db.Column(db.DateTime)

    patient = db.relationship('Patient', backref=db.backref('appointments', cascade='all, delete-orphan'))
    doctor = db.relationship('Doctor', backref=db.backref('appointments', cascade='all, delete-orphan'))

    def serialize(self):
        return {
            'id': self.id,
            'doctor_id': self.doctor_id,
            'appointment_date': self.appointment_date.isoformat() if self.appointment_date else None
        }
