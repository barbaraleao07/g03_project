# -*- coding: utf-8 -*-
"""
Created on Thu May 15 12:26:49 2025

@author: barba
"""

from classes.userlogin import Userlogin

def init_users():
    users = [
        (0, 'root', 'admin', '1234'),
        (0, 'user1', 'users', '12345')
    ]

    Userlogin.reset()

    for uid, user, group, plain_password in users:
        hashed_password = Userlogin.set_password(plain_password)

        u = Userlogin(uid, user, group, hashed_password)

        Userlogin.insert(u.id)

    print("Users initialized successfully.")

if __name__ == "__main__":
    init_users()

