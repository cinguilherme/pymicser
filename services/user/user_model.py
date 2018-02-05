import datetime
import json

"""
User Model format and basic operations

 "id": "",
    "user_names": ["name1": "name1"],
    "active": "True",
    "creatinon_date": "",
    "inative_date_start": "",
    "hashPass": ""

"""


class UserModel():

    def __init__(self):
        self.user_name_key = ""
        self.user_names = []
        self.active = True
        self.creatinon_date = "10-10-2010"
        self.inative_date_start = None
        self.hashPass = "loremipsumsofar"

    def validateJsonAdd(self, jsonAdd):
        try:
            json_object = json.loads(jsonAdd)
            self.have_essencial_keys(json_object)
            return True
        except ValueError:
            return False

    def have_essencial_keys(self, json_object):
        user_name_key = json_object['user_name_key']
        user_names = json_object['user_names']
        hashPass = json_object['hashPass']
        if user_name_key is None or user_names is None or hashPass is None:
            raise ValueError("inapropriate json")

    def new_user(self, namekey, names):
        self.user_name_key = namekey
        self.user_names = names
