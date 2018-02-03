from flask import jsonify, Blueprint, blueprints, render_template, abort, request, make_response
import json

userBP = Blueprint("userBP", __name__)

"""
UserServices BluePrint
"""

@userBP.route("/users", methods=['GET'])
def allUsers():
    with open('provisoryData/users.json') as json_data:
        j = json.load(json_data)
        return jsonify({'users': j})


@userBP.route("/users/<int:userid>", methods=['GET'])
def user(userid):
    with open('provisoryData/users.json') as json_data:
        jusers = json.load(json_data)
        user = [user for user in jusers if user['id'] == userid]

        return jsonify({'user': user})


@userBP.route("/users/add", methods=['POST'])
def add_user():
    addJson = request.json
    with open('provisoryData/users.json') as json_data:
        jusers = json.load(json_data)
        user = {
            'id': jusers[-1]['id'] + 1,
            'active': "Ture",
            'user_name': addJson.get('user_name', "")
        }
        jusers.append(user)
        return jsonify({'users': jusers}), 201


@userBP.route("/users/update/<int:userid>", methods=['PUT'])
def update_user(userid):
    updateSon = request.json
    with open('provisoryData/users.json') as json_data:
        jusers = json.load(json_data)
        user = [user for user in jusers if user['id'] == userid]

        userN = {
            'id': userid,
            'active': "Ture",
            'user_name': updateSon.get('user_name', "")
        }
        jusers[userid] = userN  # HACK horrivel, organizar isso separadamente.
        return jsonify({'users': jusers}), 201


@userBP.route("/users/delete/<int:userid>", methods=['DELETE'])
def delete_user(userid):
    with open('provisoryData/users.json') as json_data:
        jusers = json.load(json_data)
        user = [user for user in jusers if user['id'] == userid]
        de = jusers.index(user)
        del de
        return jsonify({'users': jusers}), 201
