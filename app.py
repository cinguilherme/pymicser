from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"


@app.route("/tasks", methods=['GET'])
def get_tasks():
    with opegit n('provisoryData/tasks.json') as json_data:
        j = json.load(json_data)
        return jsonify({'tasks': j})


@app.route("/users", methods=['GET'])
def get_users():
    with open('provisoryData/users.json') as json_data:
        j = json.load(json_data)
        return jsonify({'users': j})


if __name__ == "__main__":
    app.run(debug=True)
