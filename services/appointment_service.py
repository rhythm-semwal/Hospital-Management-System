from models.models import Appointment, Patient, Doctor
from database import db


class AppointmentService:
    @staticmethod
    def book_appointment(patient_id, doctor_id, appointment_date):
        try:
            appointment = Appointment(patient_id=patient_id, doctor_id=doctor_id, appointment_date=appointment_date)
            db.session.add(appointment)
            db.session.commit()
            return True, None

        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def get_patient_appointments(patient_id):
        patient = Patient.query.get(patient_id)

        if patient:
            return [appointment.serialize() for appointment in patient.appointments_assigned]
        else:
            return None

    @staticmethod
    def get_doctor_appointments(doctor_id):
        doctor = Doctor.query.get(doctor_id)

        if doctor:
            return [appointment.serialize() for appointment in doctor.appointments]
        else:
            return None
