import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

from flask import Flask, jsonify, request
from models import init_db, add_task, get_all_tasks, mark_complete, delete_task

app = Flask(__name__)
init_db()

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True)

    if not data or "title" not in data:
        logger.warning("Task creation failed: missing title")
        return jsonify({"error": "title is required"}), 400

    task = add_task(data["title"])

    if task is None:
        logger.warning("Task creation failed: empty title")
        return jsonify({"error": "title cannot be empty"}), 400

    logger.info(f"Task created: id={task['id']}, title={task['title']}")
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def list_tasks():
    tasks = get_all_tasks()
    return jsonify(tasks), 200

@app.route("/tasks/<int:task_id>/complete", methods=["PATCH"])
def complete_task(task_id):
    success = mark_complete(task_id)

    if not success:
        logger.warning(f"Mark complete failed: task {task_id} not found")
        return jsonify({"error": "task not found"}), 404

    logger.info(f"Task marked complete: id={task_id}")
    return jsonify({"message": "task marked as complete"}), 200

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def remove_task(task_id):
    success = delete_task(task_id)

    if not success:
        logger.warning(f"Delete failed: task {task_id} not found")
        return jsonify({"error": "task not found"}), 404

    logger.info(f"Task deleted: id={task_id}")
    return jsonify({"message": "task deleted"}), 200

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)