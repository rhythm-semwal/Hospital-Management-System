import os
from flask import Flask
from routes.routes import patients_bp, doctors_bp, departments_bp, appointments_bp, search_bp
from database import db, migrate

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_RECORD_QUERIES"] = True

    # app.config.from_object(Config)

    # db = SQLAlchemy(app)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        try:
            from models.models import Patient
            db.create_all()
        except Exception as exception:
            print("got the following exception when attempting db.create_all() in __init__.py: " + str(exception))
        finally:
            print("db.create_all() in __init__.py was successfull - no exceptions were raised")

    app.register_blueprint(patients_bp)
    app.register_blueprint(doctors_bp)
    app.register_blueprint(departments_bp)
    app.register_blueprint(appointments_bp)
    app.register_blueprint(search_bp)

    @app.route('/', methods=['GET'])
    def index():
        return {'message': 'Hello World!'}

    return app


if __name__ == '__main__':
    # db.create_all()
    app = create_app()
    app.run(debug=True)
