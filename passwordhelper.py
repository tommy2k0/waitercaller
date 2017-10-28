# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:11:51 2017

@author: Lenovo
"""

import hashlib
import os
import base64

class PasswordHelper:
    
    def get_hash(self, plain):
        return hashlib.sha512(str(plain).encode('utf-8')).hexdigest()
    
    def get_salt(self):
        salt = base64.b64encode(os.urandom(20))
        return str(salt)
    
    def validate_password(self, plain, salt, expected):
        return self.get_hash(plain + salt) == expected
