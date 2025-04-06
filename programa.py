# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 16:38:53 2025

@author: barba
"""

import sqlite3
from patient import Patient

def test_patient_in_database(patient_id):
    conn = sqlite3.connect('Patient.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Patient WHERE patient_id = ?", (patient_id,))
    row = cursor.fetchone()

    if row is not None:
        print(f"Patient with ID {patient_id} found in database:")
        print(f"Patient Name: {row[1]}")
        print(f"Age: {row[2]}")
        print(f"Diagnosis: {row[3]}")
        print(f"Condition: {row[4]}")
        print(f"Ward ID: {row[5]}")
    else:
        print(f"Patient with ID {patient_id} not found in database.")


    conn.close()

patient_id_to_test = 1
test_patient_in_database(patient_id_to_test)

from doctor import Doctor

conn = sqlite3.connect('Patient.db')
cur = conn.cursor()

def test_doctor():
    doctor1 = Doctor(doctor_id=1, doctor_name="Dr. John Doe", specialization="Cardiology")
    doctor2 = Doctor(doctor_id=2, doctor_name="Dr. Jane Smith", specialization="Neurology")
    
    doctor1.save_to_db(cur)
    doctor2.save_to_db(cur)
    
    conn.commit()

    cur.execute("SELECT * FROM Doctor;")
    doctors = cur.fetchall()

    if doctors:
        print("Doctors in the database:")
        for doctor in doctors:
            print(doctor)
    else:
        print("No doctors found in the database.")

test_doctor()

conn.close()

from ward import Ward

conn = sqlite3.connect('Patient.db')
cur = conn.cursor()

def test_ward():
    ward1 = Ward(ward_id=1, ward_name="Cardiology", floor=2)
    ward2 = Ward(ward_id=2, ward_name="Neurology", floor=3)
    
    ward1.save_to_db(cur)
    ward2.save_to_db(cur)
    
    conn.commit()

    cur.execute("SELECT * FROM Ward;")
    wards = cur.fetchall()

    if wards:
        print("Wards in the database:")
        for ward in wards:
            print(ward)
    else:
        print("No wards found in the database.")

test_ward()

conn.close()

from appointment import Appointment

conn = sqlite3.connect('Patient.db')
cur = conn.cursor()

def test_appointment():
    appointment1 = Appointment(appointment_date="2025-04-06", patient_id=1, doctor_id=2, ward_id=3)
    appointment2 = Appointment(appointment_date="2025-04-07", patient_id=2, doctor_id=1, ward_id=2)
    
    appointment1.save_to_db(cur)
    appointment2.save_to_db(cur)
    
    conn.commit()

    cur.execute("SELECT * FROM Appointment;")
    appointments = cur.fetchall()

    print("\nAppointments na base de dados:")
    for appointment in appointments:
        print(appointment)

test_appointment()

conn.close()



