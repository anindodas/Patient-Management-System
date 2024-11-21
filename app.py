from flask import Flask, render_template, request, redirect, url_for, session, flash
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for session management

# Initialize Firebase
cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Predefined doctor login credentials
DOCTOR_CREDENTIALS = {"username": "doctor", "password": "123"}

# Routes
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    if username == DOCTOR_CREDENTIALS['username'] and password == DOCTOR_CREDENTIALS['password']:
        session['user'] = username
        return redirect(url_for('home'))
    else:
        flash("Invalid credentials. Please try again.")
        return redirect(url_for('login'))

@app.route('/home', methods=['GET', 'POST'])
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Add patient data to Firestore
        name = request.form['name']
        age = request.form['age']
        diagnosis = request.form['diagnosis']
        patient_data = {'name': name, 'age': age, 'diagnosis': diagnosis}

        db.collection('patients').add(patient_data)
        flash("Patient data added successfully.")

    # Retrieve all patient data from Firestore
    patients = db.collection('patients').stream()
    patient_list = [patient.to_dict() for patient in patients]

    return render_template('home.html', patients=patient_list)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
