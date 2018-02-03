
"""
    Este modulo é responsavel por qualquer interação com o DB de usuarios
"""
from flask import jsonify
import json
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from bson import ObjectId

import datetime

mongo_client = MongoClient('localhost', 27017)

db = mongo_client['user-service-f-db']

userColection = db['user']

"""
get all registries of users
"""
def get_all_users():
    return dumps(userColection.find())