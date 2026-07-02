from flask import Flask, jsonify, request
from models import init_db, add_task, get_all_tasks, mark_complete

app = Flask(__name__)
init_db()

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json(silent=True)

    if not data or 'title' not in data:
        return jsonify({"error": "title is required"}), 400

    task = add_task(data['title'])

    if task is None:
        return jsonify({"error": "Title can't be empty"}), 400

    return jsonify(task), 201