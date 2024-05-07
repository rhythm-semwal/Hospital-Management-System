from models import Department, Doctor
from database import db


class DepartmentService:

    @staticmethod
    def get_all_departments(page=1, per_page=10):
        try:
            departments = Department.query.paginate(page=page, per_page=per_page)
            serialized_departments = []

            for department in departments.items:
                serialized_result = {
                    'id': department.id,
                    'name': department.name,
                    'services_offered': department.services_offered
                }

                doctors = Doctor.query.filter_by(department_id=department.id).all()

                serialized_doctors = []
                for doctor in doctors:
                    doctor_record = {
                        'id': doctor.id,
                        'name': doctor.name,
                        'specialization': doctor.specialization,
                        'contact_info': doctor.contact_info,
                        'availability_schedule': doctor.availability_schedule
                    }
                    serialized_doctors.append(doctor_record)

                serialized_result['doctors'] = serialized_doctors

                serialized_departments.append(serialized_result)

            return serialized_departments, 200
        except Exception as e:
            return {'error': f'Failed to retrieve department: {str(e)}'}, 500

    @staticmethod
    def add_department(**kwargs):
        try:
            new_department = Department(**kwargs)
            db.session.add(new_department)
            db.session.commit()
            return True, None
        except Exception as e:
            db.session.rollback()
            return False, str(e)

    @staticmethod
    def get_department(department_id):
        try:
            department = Department.query.get(department_id)

            if department is None:
                return {'error': 'Department not found'}, 404

            serialized_department = {
                'id': department.id,
                'name': department.name,
                'services_offered': department.services_offered
            }

            doctors = Doctor.query.filter_by(department_id=department_id).all()
            serialized_doctors = []
            for doctor in doctors:
                serialized_doctors.append({
                    'id': doctor.id,
                    'name': doctor.name,
                    'specialization': doctor.specialization,
                    'contact_info': doctor.contact_info,
                    'availability_schedule': doctor.availability_schedule
                })

            serialized_department["doctors"] = serialized_doctors
            return serialized_department, 200
        except Exception as e:
            return {'error': f'Failed to retrieve department: {str(e)}'}, 500

    @staticmethod
    def update_department(department_id, data):
        try:
            department = Department.query.get(department_id)
            if not department:
                return False, 'Department not found'

            for key, value in data.items():
                if hasattr(department, key):
                    setattr(department, key, value)

            db.session.commit()
            return True, 'Department updated successfully'
        except Exception as e:
            db.session.rollback()
            return False, f'Error updating Department: {str(e)}'

    @staticmethod
    def assign_doctor_to_department(department_id, doctor_id):
        try:
            department = Department.query.get(department_id)
            if not department:
                return False, 'Department not found'
            doctor = Doctor.query.get(doctor_id)
            if not doctor:
                return False, 'Doctor not found'

            doctor.department_id = department.id
            db.session.commit()
            return True, f'Doctor {doctor.name} Assigned Successfully to {department.name} Department'
        except Exception as e:
            db.session.rollback()
            return False, f'Error while assigning Doctor to Department: {str(e)}'

    @staticmethod
    def get_services_offered(department_id):
        try:
            department = Department.query.get(department_id)
            if department is None:
                return {'error': 'Department not found'}, 404
            return {'services_offered': department.services_offered}, 200
        except Exception as e:
            return {'error': f'Failed to retrieve department: {str(e)}'}, 500
