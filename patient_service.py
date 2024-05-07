from models import Patient, MedicalHistory
from database import db


class PatientService:
    @staticmethod
    def get_all_patients(page=1, per_page=10):
        try:
            patients = Patient.query.paginate(page=page, per_page=per_page)
            serialized_patients = []

            for patient in patients.items:
                serialized_patients.append(
                    {'id': patient.id,
                     'name': patient.name,
                     'age': patient.age,
                     'gender': patient.gender
                     })

            return serialized_patients, 200
        except Exception as e:
            return {'error': f'Failed to retrieve doctors: {str(e)}'}, 500

    @staticmethod
    def add_patient(**kwargs):
        try:
            new_patient = Patient(**kwargs)
            db.session.add(new_patient)
            db.session.commit()
            return True, None
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def get_patient(patient_id):
        try:
            patient = Patient.query.get(patient_id)

            if patient:
                return {'id': patient.id, 'name': patient.name, 'age': patient.age, 'gender': patient.gender}, 200
            else:
                return {'error': 'Patient not found'}, 404
        except Exception as e:
            return {'error': f'Failed to retrieve Patient: {str(e)}'}, 500

    @staticmethod
    def update_patient(patient_id, data):
        try:
            patient = Patient.query.get(patient_id)
            if not patient:
                return False, 'Patient not found'

            for key, value in data.items():
                if hasattr(patient, key):
                    setattr(patient, key, value)

            db.session.commit()
            return True, 'Patient updated successfully'
        except Exception as e:
            db.session.rollback()
            return False, f'Error updating patient: {str(e)}'

    @staticmethod
    def add_medical_history(patient_id, diagnosis, allergies, medications):
        try:
            patient = Patient.query.get(patient_id)

            if not patient:
                return False, 'Patient not found'

            new_medical_history = MedicalHistory(patient_id=patient_id, diagnosis=diagnosis,
                                                 allergies=allergies, medications=medications)

            db.session.add(new_medical_history)
            db.session.commit()

            return True, None

        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def get_medical_history(patient_id):
        try:
            patient = Patient.query.get(patient_id)

            if not patient:
                return {'error': 'Patient not found'}, 404

            medical_history = patient.medical_history_entries
            return [history.serialize() for history in medical_history] if medical_history else [], 200
        except Exception as e:
            return {'error': f'Failed to retrieve Patient: {str(e)}'}, 500
