from datetime import datetime

from flask import Blueprint, jsonify, request

patients_bp = Blueprint('patients', __name__)
doctors_bp = Blueprint('doctors', __name__)
departments_bp = Blueprint('departments', __name__)
appointments_bp = Blueprint('appointments', __name__)
search_bp = Blueprint('search', __name__)

from services.patient_service import PatientService
from services.doctor_service import DoctorService
from services.department_service import DepartmentService
from services.appointment_service import AppointmentService


# ------------------------------------- Patient Routes ------------------------------
@patients_bp.route('/patients', methods=['GET'])
def get_all_patients():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    serialized_patients, status_code = PatientService.get_all_patients(page=page, per_page=per_page)
    if status_code == 200:
        return jsonify(serialized_patients), status_code
    else:
        return jsonify(serialized_patients), status_code


@patients_bp.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is empty'}), 400

    required_fields = ['name', 'age', 'gender', 'contact_info']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing {field} in request body'}), 400

    name = data['name']
    age = data['age']
    gender = data['gender']
    contact_info = data['contact_info']

    success, message = PatientService.add_patient(name=name, age=age,
                                                  gender=gender, contact_info=contact_info)
    if success:
        return jsonify({'message': 'Patient added successfully'}), 201
    else:
        return jsonify({'error': f'Failed to add patient: {message}'}), 500


@patients_bp.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    try:
        patient, status_code = PatientService.get_patient(patient_id)

        if status_code == 200:
            return jsonify(patient), status_code
        else:
            return jsonify(patient), status_code
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@patients_bp.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body is empty'}), 400

        success, message = PatientService.update_patient(patient_id, data)

        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'error': message}), 404
    except Exception as e:
        return jsonify({'error': f'Internal Server Error: {str(e)}'}), 500


@patients_bp.route('/patients/<int:patient_id>/medical_history', methods=['POST'])
def add_medical_history(patient_id):
    data = request.get_json()

    if not data:
        return jsonify({'error': 'Request body is empty'}), 400

    required_fields = ['diagnosis', 'allergies', 'medications']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing {field} in request body'}), 400

    diagnosis = data['diagnosis']
    allergies = data['allergies']
    medications = data['medications']

    try:
        success, message = PatientService.add_medical_history(patient_id, diagnosis, allergies, medications)

        if success:
            return jsonify({'message': 'Medical history added successfully'}), 201
        else:
            return jsonify({'error': f'Failed to add medical history: {message}'}), 400

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@patients_bp.route('/patients/<int:patient_id>/medical_history', methods=['GET'])
def get_medical_history(patient_id):
    try:
        medical_history, status_code = PatientService.get_medical_history(patient_id)
        if status_code == 200:
            return jsonify(medical_history), status_code
        else:
            return jsonify(medical_history), status_code
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


# ------------------------------------- Doctor Routes ------------------------------


@doctors_bp.route('/doctors', methods=['GET'])
def get_all_doctors():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    serialized_doctors, status_code = DoctorService.get_all_doctors(page=page, per_page=per_page)
    if status_code == 200:
        return jsonify(serialized_doctors), status_code
    else:
        return jsonify(serialized_doctors), status_code


@doctors_bp.route('/doctors', methods=['POST'])
def add_doctor():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is empty'}), 400

    required_fields = ['name', 'specialization', 'contact_info', 'availability_schedule']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({'error': f'Missing fields in request body: {", ".join(missing_fields)}'}), 400

    try:
        success, message = DoctorService.add_doctor(**data)
        if success:
            return jsonify({'message': 'Doctor added successfully'}), 201
        else:
            return jsonify({'error': f'Failed to add Doctor: {message}'}), 500
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@doctors_bp.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    try:
        doctor, status_code = DoctorService.get_doctor(doctor_id)

        if status_code == 200:
            return jsonify(doctor), status_code
        else:
            return jsonify(doctor), status_code
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@doctors_bp.route('/doctors/<int:doctor_id>', methods=['PUT'])
def update_doctor(doctor_id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body is empty'}), 400

        success, message = DoctorService.update_doctor(doctor_id, data)

        if success:
            return jsonify({'message': message}), 200
        else:
            return jsonify({'error': message}), 404
    except Exception as e:
        return jsonify({'error': f'Internal Server Error: {str(e)}'}), 500


@doctors_bp.route('/doctors/<int:doctor_id>/schedule', methods=['GET'])
def availability_schedule(doctor_id):
    try:
        doctor, status_code = DoctorService.get_availability_schedule(doctor_id)

        if status_code == 200:
            return jsonify(doctor), status_code
        else:
            return jsonify(doctor), status_code
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@doctors_bp.route('/doctors/<int:doctor_id>/patients', methods=['GET'])
def get_assigned_patients(doctor_id):
    try:
        patients_list, status_code = DoctorService.get_assigned_patients(doctor_id)

        if status_code == 200:
            return jsonify(patients_list), status_code
        else:
            return jsonify(patients_list), status_code
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@doctors_bp.route('/doctors/<int:doctor_id>/patients/<int:patient_id>', methods=['POST'])
def assign_patient_to_doctor(doctor_id, patient_id):
    try:
        status, message = DoctorService.assign_patient_to_doctor(doctor_id, patient_id)

        if status:
            return jsonify({"message": message}), 200
        else:
            return jsonify({'error': message}), 500
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


# ------------------------------------- Department Routes ------------------------------
@departments_bp.route('/departments', methods=['GET'])
def list_all_departments():
    try:
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        serialized_doctors, status_code = DepartmentService.get_all_departments(page=page, per_page=per_page)
        if status_code == 200:
            return jsonify(serialized_doctors), status_code
        else:
            return jsonify(serialized_doctors), status_code
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@departments_bp.route('/departments', methods=['POST'])
def add_department():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Request body is empty'}), 400

    required_fields = ['name']
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        return jsonify({'error': f'Missing fields in request body: {", ".join(missing_fields)}'}), 400

    try:
        success, message = DepartmentService.add_department(**data)
        if success:
            return jsonify({'message': 'Department added successfully'}), 201
        else:
            return jsonify({'error': f'Failed to add Department: {message}'}), 500
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@departments_bp.route('/departments/<int:department_id>', methods=['GET'])
def get_department(department_id):
    try:
        department, status_code = DepartmentService.get_department(department_id)

        if status_code == 200:
            return jsonify(department), status_code
        else:
            return jsonify(department), status_code
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@departments_bp.route('/departments/<int:department_id>/assign_doctor', methods=['POST'])
def assign_doctor_to_department(department_id):
    try:
        data = request.get_json()
        doctor_id = data.get('doctor_id')

        if not doctor_id:
            return jsonify({'error': 'Doctor ID is required'}), 400

        status, message = DepartmentService.assign_doctor_to_department(department_id, doctor_id)

        if status:
            return jsonify({"message": message}), 200
        else:
            return jsonify({'error': message}), 500
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@departments_bp.route('/departments/<int:department_id>/services', methods=['GET'])
def get_services_offered(department_id):
    try:
        services_offered, status_code = DepartmentService.get_services_offered(department_id)

        if status_code == 200:
            return jsonify(services_offered), status_code
        else:
            return jsonify(services_offered), status_code
    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


# ------------------------------ Appointment ------------------------------------

@appointments_bp.route('/book_appointment', methods=['POST'])
def book_appointment():
    data = request.get_json()

    if not data or 'patient_id' not in data or 'doctor_id' not in data or 'appointment_date' not in data:
        return jsonify({'error': 'Invalid request data'}), 400

    patient_id = data['patient_id']
    doctor_id = data['doctor_id']
    appointment_date_str = data['appointment_date']

    try:
        appointment_date = datetime.fromisoformat(appointment_date_str)

        success, message = AppointmentService.book_appointment(patient_id, doctor_id, appointment_date)

        if success:
            return jsonify({'message': 'Appointment booked successfully'}), 201
        else:
            return jsonify({'error': f'Failed to book appointment: {message}'}), 500

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@appointments_bp.route('/patients/<int:patient_id>/appointments', methods=['GET'])
def get_patient_appointments(patient_id):
    try:
        appointments = AppointmentService.get_patient_appointments(patient_id)

        if appointments:
            return jsonify(appointments), 200
        else:
            return jsonify({'message': 'No appointments found for the patient'}), 404

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@appointments_bp.route('/doctors/<int:doctor_id>/appointments', methods=['GET'])
def get_doctor_appointments(doctor_id):
    try:
        appointments = AppointmentService.get_doctor_appointments(doctor_id)

        if appointments:
            return jsonify(appointments), 200
        else:
            return jsonify({'message': 'No appointments found for the doctor'}), 404

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

# ------------------------- Search -------------------


@search_bp.route('/search/patients', methods=['GET'])
def search_patients():
    filter_criteria = {}
    for key in request.args:
        filter_criteria[key] = request.args[key]

    page = int(filter_criteria.pop('page', 1))
    limit = int(filter_criteria.pop('limit', 10))
    limit = min(limit, 100)

    patients = PatientService.search_patients(filter_criteria, page=page, per_page=limit)

    return jsonify(patients), 200


@search_bp.route('/search/doctors', methods=['GET'])
def search_doctors():
    filter_criteria = {}
    for key in request.args:
        filter_criteria[key] = request.args[key]

    page = int(filter_criteria.pop('page', 1))
    limit = int(filter_criteria.pop('limit', 10))
    limit = min(limit, 100)

    doctors = DoctorService.search_doctors(filter_criteria, page=page, per_page=limit)

    return jsonify(doctors), 200


@search_bp.route('/search/departments', methods=['GET'])
def search_departments():
    filter_criteria = {}
    for key in request.args:
        filter_criteria[key] = request.args[key]

    page = int(filter_criteria.pop('page', 1))
    limit = int(filter_criteria.pop('limit', 10))
    limit = min(limit, 100)

    departments = DepartmentService.search_departments(filter_criteria, page=page, per_page=limit)

    return jsonify(departments), 200
