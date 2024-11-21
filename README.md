# Patient Management System

This is a simple Flask-based web application for a **Patient Management System**. The application allows doctors to log in using predefined credentials, manage patient data, and store it in Firebase Firestore.

## Features

- **Doctor Login**: A simple login page where doctors can log in using predefined credentials.
- **Patient Management**: Once logged in, doctors can add patient data (name, age, diagnosis) to the system.
- **Patient Records**: Display a list of all added patients with their details.
- **Session Management**: Uses Flask's session management to keep track of logged-in doctors.

## Folder Structure

patient_management_app/ |-- app.py # Main Flask application |-- templates/ | |-- login.html # Login page template | |-- home.html # Doctor's home page template |-- serviceAccountKey.json # Firebase service account key |-- requirements.txt # List of dependencies

bash
Copy code

## Requirements

To run this project, you need the following installed on your machine:

- Python 3.7 or higher
- Firebase Project with Firestore enabled
- A Firebase service account key (`serviceAccountKey.json`)

## Setup & Installation

### 1. Clone the Repository

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/anindodas/Patient-Management-System.git
cd Patient-Management-System
```

## 2. Create and Activate a Virtual Environment
For managing dependencies, it is recommended to use a virtual environment:

python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
Install the required Python packages by running:
```bash
pip install -r requirements.txt
```
4. Firebase Setup
Create a Firebase project in the Firebase Console.
Enable Firestore in your Firebase project.
Generate a Service Account Key:
Go to the Project Settings in Firebase.
Navigate to the Service Accounts tab and generate a new private key.
Download the JSON key and place it in the root of the project as serviceAccountKey.json.


5. Running the App
Once everything is set up, you can run the Flask application
```bash
python app.py
```


By default, the app will be available at http://127.0.0.1:5000/.

6. Accessing the App
Visit http://127.0.0.1:5000/ in your browser.
Log in with the predefined credentials:
Username: doctor
Password: 123
After logging in, you can add patient details and view a list of all patients.
How It Works
Login Page: The app presents a login page (login.html). The predefined credentials are checked when the doctor tries to log in.
Doctor Panel: Upon successful login, the doctor is redirected to the home page (home.html), where they can add new patient data (name, age, diagnosis).
Firestore Integration: Patient data is stored in Firebase Firestore under the collection patients.
Session Management: The app uses Flask's session mechanism to keep track of the doctor's login status.
Technologies Used
Flask: Web framework for Python.
Firebase Firestore: NoSQL cloud database for storing patient records.
HTML/CSS: For the frontend interface
