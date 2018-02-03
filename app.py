from flask import Flask, jsonify, make_response, request
import json

import services.userservice as users


app = Flask(__name__)

app.register_blueprint(users.userBP)


@app.route("/")
def index():
    return "hello world"


@app.route("/tasks", methods=['GET'])
def get_tasks():
    with open('provisoryData/tasks.json') as json_data:
        j = json.load(json_data)
        return jsonify({'tasks': j})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'API function Not found'}), 404)

if __name__ == "__main__":
    app.run(debug=True)
