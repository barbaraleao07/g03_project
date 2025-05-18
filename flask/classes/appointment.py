# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 21:49:15 2025

@author: barba
"""

from classes.gclass import Gclass
import datetime
class Appointment(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_id', '_appointment_date', '_patient_id', '_doctor_id', '_ward_id']
    
    header = 'Appointment'
    
    des = ['Id', 'Date', 'Patient', 'Doctor', 'Ward']

    def __init__(self, appointment_id,appointment_date, patient_id, doctor_id, ward_id):
        super().__init__()
        appointment_id = Appointment.get_id(appointment_id)
        self._id = appointment_id
        self._appointment_date =str(appointment_date)
        self._patient_id = patient_id
        self._doctor_id = doctor_id
        self._ward_id = ward_id

    @property
    def id(self):
        return self._id

    @property
    def appointment_date(self):
        return self._appointment_date
    @appointment_date.setter
    def appointment_date(self, appointment_date):
        self._appointment_date = datetime.date.fromisoformat(appointment_date)

    @property
    def patient_id(self):
        return self._patient_id
    @patient_id.setter
    def patient_id(self, patient_id):
        self._patient_id = patient_id

    @property
    def doctor_id(self):
        return self._doctor_id
    @doctor_id.setter
    def doctor_id(self, doctor_id):
        self._doctor_id = doctor_id

    @property
    def ward_id(self):
        return self._ward_id
    @ward_id.setter
    def ward_id(self, ward_id):
        self._ward_id = ward_id

    def save_to_db(self,cursor):
        insert_condition = """INSERT INTO Appointment(patient_id, doctor_id, appointment_date,ward_id) VALUES (?, ?, ?, ?);"""
        
        data_tuple = (self.patient_id, self.doctor_id, self.appointment_date, self.ward_id)
        cursor.execute(insert_condition, data_tuple)

