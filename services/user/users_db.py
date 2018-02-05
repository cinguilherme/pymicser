
"""
    Este modulo é responsavel por qualquer interação com o DB de usuarios
"""
from flask import jsonify
import json
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
from bson import ObjectId
from services.user.user_model import UserModel

import datetime

mongo_client = MongoClient('localhost', 27017)

db = mongo_client['user-service-f-db']

userColection = db['user']


def get_all_users():
    return dumps(userColection.find())


def get_user_by_id(id):
    return dumps(userColection.find_one({"_id": id}))


def get_user_by_user_name(username):
    return dumps(userColection.find_one({"user_names": username}))


def add_new_user(jsonNUser):
    model = UserModel()
    if model.validateJsonAdd(jsonNUser):
        return dumps(userColection.insert(jsonNUser))


def update_user(userObject):
    pass
