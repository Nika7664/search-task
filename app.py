from flask import Flask, jsonify
import requests
import jsonschema
import json

app = Flask(__name__)

@app.route('/tasks', methods=['POST'])
def solve_task():
    schema = {
        "type": "object",
        "properties": {
            "task_description": {"type": "string"},
            "task_schema": {"type": "string"},
            "actions":{"type":"array", "items": {"type": "string"}},
            "max_count": {"type": "integer"}
        },
        "required": []
    }

    data = requests.get_json()
    if not data:
        return jsonify({'commandList': ['ERROR']}), 400

    try:
        jsonschema.validate(instance=data, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        return jsonify({'commandList': ['ERROR']}), 400

    result = data.get("task_description")
    return jsonify({'commandList': [result.replace("TASK", "SUCCESS")]}), 200

if __name__ == '__main__':
    app.run(debug=True, port=8080)