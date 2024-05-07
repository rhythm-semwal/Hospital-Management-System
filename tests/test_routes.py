import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_all_patients(self):
        response = self.app.get('/patients')
        self.assertEqual(response.status_code, 200)

    def test_add_patient(self):
        patient_data = {
            'name': 'John Doe',
            'age': 30,
            'gender': 'Male',
            'contact_info': '1234567890'
        }
        response = self.app.post('/patients', json=patient_data)
        self.assertEqual(response.status_code, 201)

    def test_get_patient(self):
        response = self.app.get('/patients/1')
        self.assertEqual(response.status_code, 200)

    # Add more test cases for other patient routes (e.g., update_patient, add_medical_history, get_medical_history)

    def test_get_all_doctors(self):
        response = self.app.get('/doctors')
        self.assertEqual(response.status_code, 200)

    def test_add_doctor(self):
        doctor_data = {
            'name': 'Dr. Smith',
            'specialization': 'Cardiology',
            'contact_info': '9876543210',
            'availability_schedule': {
                'monday': '9:00 AM - 5:00 PM',
                'tuesday': '9:00 AM - 5:00 PM',
                'wednesday': '9:00 AM - 1:00 PM',
                'thursday': '9:00 AM - 5:00 PM',
                'friday': '9:00 AM - 5:00 PM'
            }
        }
        response = self.app.post('/doctors', json=doctor_data)
        self.assertEqual(response.status_code, 201)

    def test_get_doctor(self):
        response = self.app.get('/doctors/1')
        self.assertEqual(response.status_code, 200)

    # Add more test cases for other doctor routes (e.g., update_doctor, availability_schedule, get_assigned_patients)

    def test_list_all_departments(self):
        response = self.app.get('/departments')
        self.assertEqual(response.status_code, 200)

    def test_add_department(self):
        department_data = {
            'name': 'Cardiology'
        }
        response = self.app.post('/departments', json=department_data)
        self.assertEqual(response.status_code, 201)

    def test_get_department(self):
        response = self.app.get('/departments/1')
        self.assertEqual(response.status_code, 200)

    # Add more test cases for other department routes (e.g., assign_doctor_to_department, get_services_offered)

    def test_book_appointment(self):
        appointment_data = {
            'patient_id': 1,
            'doctor_id': 1,
            'appointment_date': '2024-05-15T10:00:00'
        }
        response = self.app.post('/book_appointment', json=appointment_data)
        self.assertEqual(response.status_code, 201)

    # Add more test cases for other appointment routes (e.g., get_patient_appointments, get_doctor_appointments)

    def test_search_patients(self):
        response = self.app.get('/search/patients?page=1&limit=10')
        self.assertEqual(response.status_code, 200)

    def test_search_doctors(self):
        response = self.app.get('/search/doctors?page=1&limit=10')
        self.assertEqual(response.status_code, 200)

    def test_search_departments(self):
        response = self.app.get('/search/departments?page=1&limit=10')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
