import json

from models import Doctor, Patient
from database import db


class DoctorService:

    @staticmethod
    def get_all_doctors(page=1, per_page=10):

        try:
            doctors = Doctor.query.paginate(page=page, per_page=per_page)
            serialized_doctors = []

            for doctor in doctors.items:
                serialized_doctors.append({
                    'id': doctor.id,
                    'name': doctor.name,
                    'specialization': doctor.specialization,
                    'contact_info': doctor.contact_info,
                    'availability_schedule': doctor.availability_schedule,
                    'department_id': doctor.department_id
                })

            return serialized_doctors, 200
        except Exception as e:
            return {'error': f'Failed to retrieve doctors: {str(e)}'}, 500

    @staticmethod
    def add_doctor(**kwargs):
        try:
            new_doctor = Doctor(**kwargs)
            db.session.add(new_doctor)
            db.session.commit()
            return True, None
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def get_doctor(doctor_id):
        try:
            doctor = Doctor.query.get(doctor_id)

            if doctor is None:
                return {'error': 'Doctor not found'}, 404

            return {
                'id': doctor.id,
                'name': doctor.name,
                'specialization': doctor.specialization,
                'contact_info': doctor.contact_info,
                'availability_schedule': doctor.availability_schedule,
                'department_id': doctor.department_id
            }, 200
        except Exception as e:
            return {'error': f'Failed to retrieve Doctor: {str(e)}'}, 500

    @staticmethod
    def update_doctor(doctor_id, data):
        try:
            doctor = Doctor.query.get(doctor_id)
            if not doctor:
                return False, 'Doctor not found'

            for key, value in data.items():
                if hasattr(doctor, key):
                    setattr(doctor, key, value)

            db.session.commit()
            return True, 'doctor updated successfully'
        except Exception as e:
            db.session.rollback()
            return False, f'Error updating doctor: {str(e)}'

    @staticmethod
    def get_availability_schedule(doctor_id):
        try:
            doctor = Doctor.query.get(doctor_id)
            if doctor:
                return doctor.availability_schedule, 200
            else:
                return {'message': 'Doctor Not Found'}, 404
        except Exception as e:
            return {'error': f'Failed to retrieve Availability schedule for {doctor.name}: {str(e)}'}, 500

    @staticmethod
    def get_assigned_patients(doctor_id):
        try:
            doctor = Doctor.query.get(doctor_id)
            if not doctor:
                return {'message': 'Doctor Not Found'}, 404

            patients = doctor.patients
            return [patient.serialize() for patient in patients] if patients else [], 200
        except Exception as e:
            return {'error': f'Failed to retrieve List Of Patients Assigned for {doctor.name}: {str(e)}'}, 500

    @staticmethod
    def assign_patient_to_doctor(doctor_id, patient_id):
        try:
            doctor = Doctor.query.get(doctor_id)
            if not doctor:
                return False, 'Doctor not found'

            patient = Patient.query.get(patient_id)
            if not patient:
                return False, 'Patient not found'

            doctor.patient_id = patient.id
            db.session.commit()
            return True, f'Patient {patient.name} Assigned Successfully to Dr.{doctor.name}'
        except Exception as e:
            db.session.rollback()
            return False, f'Error while assigning Patient to Doctor: {str(e)}'
