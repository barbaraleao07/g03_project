# -*- coding: utf-8 -*-
"""
Created on Mon May 12 14:41:31 2025

@author: barba
"""

import bcrypt
from classes.gclass import Gclass

class Userlogin(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''

    att = ['_id', '_user','_usergroup','_password']

    header = 'Users'

    des = ['Id', 'User','User group','Password']
    username = ''
    user_id = 0

    def __init__(self, id, user, usergroup, password):
        super().__init__()
        id = Userlogin.get_id(int(id))
        self._id = id
        self._user = user
        self._usergroup = usergroup
        self._password = password
        Userlogin.obj[id] = self
        Userlogin.lst.append(id)


    @property
    def id(self):
        return self._id

    @property
    def user(self):
        return self._user

    @property
    def usergroup(self):
        return self._usergroup
    @usergroup.setter
    def usergroup(self, usergroup):
        self._usergroup = usergroup
        
    @property
    def password(self):
        return ""
    
    @password.setter
    def password(self, password):
        self._password = password

    @classmethod
    def get_user_id(cls, user):
        user_id = 0
        lsobj = Userlogin.find(user, 'user')
        if len(lsobj) == 1:
            obj = lsobj[0]
            user_id = obj.id
        return user_id            
    
    @classmethod
    def chk_password(cls, user, password):
        Userlogin.username = ''
        user_id = Userlogin.get_user_id(user)
        if user_id != 0:
            obj = Userlogin.obj[user_id]
            valid = bcrypt.checkpw(password.encode(), obj._password.encode())
            if valid:
                Userlogin.user_id = obj.id
                Userlogin.username = obj.user
                message = "Valid"
            else:
                message = 'Wrong password'
        else:
            message = 'No existent user'
        return message
    
    @classmethod
    def set_password(cls, password):
        passencrypted = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return passencrypted.decode()
    
    def __str__(self):
        return f'Id:{self.id}, User:{self.user}, Usergroup:{self.usergroup}'