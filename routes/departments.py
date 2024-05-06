# from flask import Blueprint, request, jsonify
# from models import db, Department, Doctor
#
# departments_bp = Blueprint('departments', __name__, url_prefix='/departments')
#
#
# @departments_bp.route('/', methods=['GET'])
# def list_all_departments():
#     departments = Department.query.all()
#     return jsonify([department.serialize() for department in departments]), 200
#
#
# @departments_bp.route('/<int:department_id>/services', methods=['GET'])
# def get_services_offered(department_id):
#     department = Department.query.get_or_404(department_id)
#     return jsonify({'services_offered': department.services_offered}), 200
#
#
# @departments_bp.route('/<int:department_id>/assign_doctor', methods=['POST'])
# def assign_doctor_to_department(department_id):
#     data = request.get_json()
#     doctor_id = data.get('doctor_id')
#
#     if not doctor_id:
#         return jsonify({'error': 'Doctor ID is required'}), 400
#
#     doctor = Doctor.query.get_or_404(doctor_id)
#     department = Department.query.get_or_404(department_id)
#
#     doctor.department_id = department.id
#     db.session.commit()
#
#     return jsonify({'message': f'Doctor {doctor.name} assigned to department {department.name} successfully'}), 200
