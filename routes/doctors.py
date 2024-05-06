# from flask import Blueprint, request, jsonify
# from models import db, Doctor, Patient, Appointment
#
# doctors_bp = Blueprint('doctors', __name__, url_prefix='/doctors')
#
#
# @doctors_bp.route('/', methods=['GET'])
# def list_all_doctors():
#     doctors = Doctor.query.all()
#     return jsonify([doctor.serialize() for doctor in doctors]), 200
#
#
# @doctors_bp.route('/', methods=['POST'])
# def add_doctor():
#     data = request.get_json()
#
#     name = data.get('name')
#     specialization = data.get('specialization')
#     contact_info = data.get('contact_info')
#
#     if not name or not specialization or not contact_info:
#         return jsonify({'error': 'Please provide name, specialization, and contact information'}), 400
#
#     new_doctor = Doctor(name=name, specialization=specialization, contact_info=contact_info)
#     db.session.add(new_doctor)
#     db.session.commit()
#
#     return jsonify({'message': 'Doctor added successfully'}), 201
#
#
# @doctors_bp.route('/<int:doctor_id>/patients', methods=['GET'])
# def list_of_patients_assigned(doctor_id):
#     doctor = Doctor.query.get_or_404(doctor_id)
#     assigned_patients = doctor.patients
#     return jsonify([patient.serialize() for patient in assigned_patients]), 200
#
#
# @doctors_bp.route('/<int:doctor_id>/assign_patient', methods=['PUT'])
# def assign_patient_to_doctor(doctor_id):
#     data = request.get_json()
#     patient_id = data.get('patient_id')
#
#     if not patient_id:
#         return jsonify({'error': 'Patient ID is required'}), 400
#
#     doctor = Doctor.query.get_or_404(doctor_id)
#     patient = Patient.query.get_or_404(patient_id)
#
#     patient.doctor_id = doctor.id
#     db.session.commit()
#
#     return jsonify({'message': f'Patient {patient.name} assigned to Doctor {doctor.name} successfully'}), 200
#
#
# @doctors_bp.route('/<int:doctor_id>/schedule', methods=['GET'])
# def availability_schedule(doctor_id):
#     doctor = Doctor.query.get_or_404(doctor_id)
#     if doctor.availability_schedule:
#         return jsonify(doctor.availability_schedule), 200
#     else:
#         return jsonify({'message': 'Availability schedule not found for this doctor'}), 404
