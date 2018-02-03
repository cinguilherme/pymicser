from flask import jsonify
import json


def allUsers():
    with open('provisoryData/users.json') as json_data:
        j = json.load(json_data)
        return jsonify({'users': j})


def user(userid):
    with open('provisoryData/users.json') as json_data:
        jusers = json.load(json_data)
        user = [user for user in jusers if user['id'] == userid]
        
        return jsonify({'user': user})


def add_user(addJson):
    with open('provisoryData/users.json') as json_data:
        jusers = json.load(json_data)
        user = {
            'id' : jusers[-1]['id'] + 1,
            'active' : "Ture",
            'user_name' : addJson.get('user_name', "")
        }
        jusers.append(user)
        return jsonify({'users': jusers}), 201
