from flask import Flask
from routes.patients import patients_bp
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from models import Patient, MedicalHistory, Appointment, Doctor, Department


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


# Import and register blueprints after app and db are defined
# from routes.departments import departments_bp
# from routes.doctors import doctors_bp

app.register_blueprint(patients_bp.bp)
# app.register_blueprint(departments_bp)
# app.register_blueprint(doctors_bp)

if __name__ == '__main__':
    app.run(debug=True)
