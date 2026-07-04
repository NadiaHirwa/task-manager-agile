from flask import Flask, jsonify, request
from models import init_db, add_task, get_all_tasks, mark_complete, delete_task

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

@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = get_all_tasks()
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>/complete', methods=['PATCH'])
def complete_task(task_id):
    success = mark_complete(task_id)

    if not success:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({"message": "Task marked as complete"}), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    success = delete_task(task_id)

    if not success:
        return jsonify({"error": "task not found"}), 404

    return jsonify({"message": "task deleted"}), 200

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)