# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 21:27:56 2025

@author: barba
"""
from classes.gclass import Gclass
class Patient(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_patient_id', '_patient_name', '_age', '_diagnosis', '_condition', '_ward_id', '_user']

    header = 'Patient'

    des = ['Patient Id', 'Patient Name', 'Age', 'Diagnosis', 'Condition', 'Ward Id', 'User']

    def __init__(self, patient_id, patient_name, age, diagnosis, condition, ward_id, user):
        super().__init__()
        patient_id = Patient.get_id(patient_id)
        self._id = patient_id
        self._patient_name = patient_name
        self._age = age
        self._diagnosis = str(diagnosis)
        self._condition = str(condition)
        self._ward_id = int(ward_id)
        self._user = user

        Patient.obj[patient_id] = self
        Patient.lst.append(patient_id)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, patient_id):
        self._id = patient_id

    @property
    def patient_name(self):
        return self._patient_name
    
    @patient_name.setter
    def patient_name(self, patient_name):
        self._patient_name = patient_name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age

    @property
    def diagnosis(self):
        return self._diagnosis
    
    @diagnosis.setter
    def diagnosis(self, diagnosis):
        self._diagnosis = diagnosis

    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, condition):
        self._condition = condition
        
    @property
    def ward_id(self):
        return self._ward_id
    
    @ward_id.setter
    def ward_id(self, ward_id):
        self._ward_id = int(ward_id)
        
    @property
    def user(self):
        return self._user
        
    @classmethod
    def insert(cls, id):
        if id in cls.lst:
            return
        cls.lst.append(id)
        cls.pos = len(cls.lst) - 1

    @classmethod
    def update(cls, id):
        if id in cls.lst:
            cls.obj[id] = cls.obj[id]

    @classmethod
    def remove(cls, id):
        if id in cls.obj:
            del cls.obj[id]
            cls.lst.remove(id)
            cls.pos = max(0, cls.pos - 1)

    @classmethod
    def current(cls):
        if cls.lst:
            current_id = cls.lst[cls.pos]
            return cls.obj.get(current_id)
        return None

    @classmethod
    def first(cls):
        if cls.lst:
            cls.pos = 0

    @classmethod
    def previous(cls):
        if cls.lst and cls.pos > 0:
            cls.pos -= 1
            return True
        return False

    @classmethod
    def nextrec(cls):
        if cls.lst and cls.pos < len(cls.lst) - 1:
            cls.pos += 1

    @classmethod
    def last(cls):
        if cls.lst:
            cls.pos = len(cls.lst) - 1

    @classmethod
    def get_id(cls, base_id):
        # Retorna próximo ID disponível
        base = 1000 if base_id == 0 else base_id
        while base in cls.obj:
            base += 1
        return base
    
    def save_to_db(self,cursor):
        insert_condition = """INSERT INTO Patient(patient_id, patient_name, age, diagnosis, condition, ward_id, user) VALUES (?, ?, ?, ?, ?, ?, ?);"""

        data_tuple = (self.id, self.patient_name, self.age, self.diagnosis, self.condition, self.ward_id, self.user)
        cursor.execute(insert_condition, data_tuple)
