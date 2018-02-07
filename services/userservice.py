from flask import jsonify, Blueprint, blueprints, render_template, abort, request, make_response
import json

import services.user.users_db as db_service

userBP = Blueprint("userBP", __name__)

"""
UserServices BluePrint
"""

""" API function get all users: if unnable to fetch from NSql,
 fetch from local JSON"""

# Exemplo de retorno de documentação de um método.
@userBP.route("/users/doc", methods=['GET'])
def users_doc():
    return allUsers.__doc__

@userBP.route("/users", methods=['GET'])
def allUsers():
    """
    UserServices BluePrint

    API function get all users: if unnable to fetch from NSql,
     fetch from local JSON
    """
    try:
        return jsonify(db_service.get_all_users())
    except:
        with open('provisoryData/users.json') as json_data:
            j = json.load(json_data)
            return jsonify({'users': j})


@userBP.route("/users/<int:userid>", methods=['GET'])
def user(userid):
    with open('provisoryData/users.json') as json_data:
        jusers = json.load(json_data)
        user = [user for user in jusers if user['id'] == userid]

        return jsonify({'user': user})


@userBP.route("/users/byname/<username>", methods=['GET'])
def user_by_name(username):
    return jsonify(db_service.get_user_by_user_name(username))


@userBP.route("/users/add", methods=['POST'])
def add_user():
    addJson = request.json
    return jsonify(db_service.add_new_user(addJson)), 201


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
