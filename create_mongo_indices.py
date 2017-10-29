# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:24:34 2017

@author: Lenovo
"""

import pymongo
client = pymongo.MongoClient()
c = client['waitercaller']
print(c.users.create_index("email", unique=True))
print(c.requests.create_index("table_id", unique=True))