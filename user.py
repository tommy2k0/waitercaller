# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 21:46:08 2017

@author: Lenovo
"""

class User:
    def __init__(self,email):
        self.email = email
    
    def get_id(self):
        return self.email
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True