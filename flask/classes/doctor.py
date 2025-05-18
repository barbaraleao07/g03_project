# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 21:36:14 2025

@author: barba
"""

from classes.gclass import Gclass
class Doctor(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_doctor_id', '_doctor_name', '_specialization', '_user']

    header = 'Doctor'
    
    des = ['Doctor Id', 'Doctor Name', 'Specialization', 'User']

    def __init__(self, doctor_id, doctor_name, specialization, user):
        super().__init__()
        doctor_id = Doctor.get_id(doctor_id)
        self._id = doctor_id
        self._doctor_name = doctor_name
        self._specialization = specialization
        self._user = user
        
        Doctor.obj[doctor_id] = self
        Doctor.lst.append(doctor_id)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, doctor_id):
        self._id = doctor_id

    @property
    def doctor_name(self):
        return self._doctor_name
    @doctor_name.setter
    def doctor_name(self, doctor_name):
        self._doctor_name = doctor_name

    @property
    def specialization(self):
        return self._specialization
    @specialization.setter
    def specialization(self, specialization):
        self._specialization = specialization
        
    @property
    def user(self):
        return self._user

    def save_to_db(self,cursor):
        insert_condition = """INSERT INTO Doctor(doctor_id, doctor_name, specialization, user) VALUES (?, ?, ?, ?);"""

        data_tuple = (self.id, self.doctor_name, self.specialization, self.user)
        cursor.execute(insert_condition, data_tuple)
