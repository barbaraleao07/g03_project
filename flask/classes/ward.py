# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 21:39:59 2025

@author: barba
"""

from classes.gclass import Gclass
class Ward(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_ward_id','_ward_name','_floor']

    header = 'Ward'

    des = ['Ward Id','Ward Name','Floor']

    def __init__(self, ward_id, ward_name, floor):
        super().__init__()
        ward_id = Ward.get_id(ward_id)
        self._id = ward_id
        self._ward_name = ward_name
        self._floor = int(floor)

        Ward.obj[ward_id] = self
        Ward.lst.append(ward_id)

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, ward_id):
        self._id = ward_id

    @property
    def ward_name(self):
        return self._ward_name
    @ward_name.setter
    def ward_name(self, ward_name):
        self._ward_name = ward_name

    @property
    def floor(self):
        return self._floor
    @floor.setter
    def floor(self, floor):
        self._floor = floor

    def save_to_db(self,cursor):
        insert_condition = """INSERT INTO Ward(ward_id, ward_name, floor) VALUES (?, ?, ?);"""

        data_tuple = (self.id, self.ward_name, self.floor)
        cursor.execute(insert_condition, data_tuple)
