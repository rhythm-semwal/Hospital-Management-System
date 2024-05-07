from database import db


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    contact_info = db.Column(db.String(100))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'))

    # Relationships
    medical_history_entries = db.relationship('MedicalHistory', back_populates='patient', lazy=True,
                                              cascade='all, delete-orphan')
    appointments_assigned = db.relationship('Appointment', back_populates='patient', lazy=True,
                                            cascade='all, delete-orphan')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'contact_info': self.contact_info,
            'doctor_id': self.doctor_id,
            'medical_history': [history.serialize() for history in self.medical_history_entries],
            'appointments': [appointment.serialize() for appointment in self.appointments_assigned]
        }


class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    contact_info = db.Column(db.String(100))
    availability_schedule = db.Column(db.JSON)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'))

    # Define the relationship with Department
    department = db.relationship('Department', back_populates='doctors')

    # Relationships
    appointments = db.relationship('Appointment', back_populates='doctor', lazy=True,
                                   cascade='all, delete-orphan')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'specialization': self.specialization,
            'contact_info': self.contact_info,
            'availability_schedule': self.availability_schedule,
            'department_id': self.department_id
        }


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    services_offered = db.Column(db.String(255))

    # Relationships
    doctors = db.relationship('Doctor', back_populates='department', lazy=True)

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

    # Relationships
    patient = db.relationship('Patient', back_populates='medical_history_entries')

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

    # Relationships
    patient = db.relationship('Patient', back_populates='appointments_assigned')
    doctor = db.relationship('Doctor', back_populates='appointments')

    def serialize(self):
        return {
            'id': self.id,
            'doctor_id': self.doctor_id,
            'appointment_date': self.appointment_date.isoformat() if self.appointment_date else None
        }
