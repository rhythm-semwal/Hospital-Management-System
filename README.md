# Hospital-Management-System

### Setting Up the Application

Clone the Repository:

Begin by cloning the repository using git. If you don't have git installed, you can download it from https://git-scm.com/. Open your terminal and navigate to your desired directory. Then, run the following command:

```bash
git clone https://github.com/rhythm-semwal/flask-tutorial.git
```
### Install Dependencies:

Navigate to the project directory using the following command:

```bash
cd flask-tutorial
```

### Install the required Python libraries using pip:

```bash
pip3 install flask flask-sqlalchemy
```
### Create the Database:

```The application uses a SQLite database. By default, the database file (database.db) will be created automatically in the project directory when you run the application.```

### Running the Application
Start the Development Server:

Run the following command in your terminal to start the development server:


```bash
python3 app.py
```

This will start the Flask development server. By default, it will run on http://127.0.0.1:5000/. You can access the application in your web browser by going to this URL.

### Verify Installation:

Once the server is running, open http://127.0.0.1:5000/ in your web browser. You should see a JSON response with the message "Hello World!". This confirms that the application is running successfully.

### Project Structure
The project consists of the following files and folders:


**app.py**: This is the main Flask application file. It configures the database connection, registers blueprints for different functionalities, and defines routes.

**database.py**: This file contains the database configuration using Flask-SQLAlchemy.

**routes.py**: This file defines blueprints for managing Patients, Doctors, Departments, and Appointments. Each blueprint handles routes and logic related to its specific functionality. (This file might not be included in the current version you have)

**models.py**: This file likely defines the data models for Patients, Doctors, Departments, and Appointments. These models represent the database schema. (This file might not be included in the current version you have)




