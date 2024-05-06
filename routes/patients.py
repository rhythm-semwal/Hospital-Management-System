from flask import Blueprint, request, jsonify
from services.patient_service import PatientService

patients_bp = Blueprint('patients', __name__)


@patients_bp.route('/', methods=['GET'])
def get_all_patients():
    patients = PatientService.get_all_patients()
    return jsonify(patients), 200


# @patients_bp.route('/', methods=['POST'])
# def add_patient():
#     data = request.get_json()
#
#     name = data.get('name')
#     age = data.get('age')
#     gender = data.get('gender')
#     contact_info = data.get('contact_info')
#
#     if not name or not age or not gender or not contact_info:
#         return jsonify({'error': 'Please provide name, age, gender, and contact information'}), 400
#
#     new_patient = Patient(name=name, age=age, gender=gender, contact_info=contact_info)
#     db.session.add(new_patient)
#     db.session.commit()
#
#     return jsonify({'message': 'Patient added successfully'}), 201
#
#
# @patients_bp.route('/<int:patient_id>/medical_history', methods=['POST'])
# def add_medical_history(patient_id):
#     data = request.get_json()
#     patient = Patient.query.get_or_404(patient_id)
#
#     history = MedicalHistory(patient_id=patient.id, diagnosis=data['diagnosis'], allergies=data['allergies'],
#                              medications=data['medications'])
#     db.session.add(history)
#     db.session.commit()
#
#     return jsonify({'message': 'Medical history added successfully'}), 201
#
#
# @patients_bp.route('/<int:patient_id>/medical_history', methods=['GET'])
# def get_medical_history(patient_id):
#     patient = Patient.query.get_or_404(patient_id)
#     medical_history = patient.medical_history
#
#     return jsonify([history.serialize() for history in medical_history]), 200
#
#
# @patients_bp.route('/<int:patient_id>/appointments', methods=['POST'])
# def add_appointment(patient_id):
#     data = request.get_json()
#     patient = Patient.query.get_or_404(patient_id)
#     doctor_id = data.get('doctor_id')
#
#     # Check if the doctor_id is provided and valid
#     if not doctor_id:
#         return jsonify({'error': 'Doctor ID is required'}), 400
#
#     doctor = Doctor.query.get_or_404(doctor_id)
#
#     appointment = Appointment(patient_id=patient.id, doctor_id=doctor.id, appointment_date=data.get('appointment_date'))
#     db.session.add(appointment)
#     db.session.commit()
#
#     return jsonify({'message': 'Appointment added successfully'}), 201
#
#
# @patients_bp.route('/<int:patient_id>/appointments', methods=['GET'])
# def get_patient_appointments(patient_id):
#     patient = Patient.query.get_or_404(patient_id)
#     appointments = patient.appointments
#
#     return jsonify([appointment.serialize() for appointment in appointments]), 200


# Gemini
from flask import request, jsonify, Blueprint
from models import Patient

# bp = Blueprint('patients', __name__)
#
#
# @bp.route('/patients', methods=['POST'])
# def create_patient():
#     data = request.get_json()
#     patient = Patient(name=data['name'], age=data['age'], gender=data['gender'], contact_info=data['contact_info'])
#     db.session.add(patient)
#     db.session.commit()
#     return jsonify({'message': 'Patient created successfully', 'patient': patient.serialize()}), 201
#
# # ... other patient
