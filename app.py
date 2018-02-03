from flask import Flask, jsonify, make_response, request
import json

import services.userservice as users


app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"


@app.route("/tasks", methods=['GET'])
def get_tasks():
    with open('provisoryData/tasks.json') as json_data:
        j = json.load(json_data)
        return jsonify({'tasks': j})


@app.route("/users", methods=['GET'])
def get_users():
    return users.allUsers()


@app.route("/users/<int:userid>", methods=['GET'])
def get_user(userid):
    return users.user(userid)


@app.route("/users/add", methods=['POST'])
def add_user():
    request_post_json = request.json
    return users.add_user(request_post_json)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(debug=True)
