from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {"id": 1, "task": "Купить молоко", "done": False},
    {"id": 2, "task": "Сделать домашку", "done": True}
]
@app.route('/')
def home():
    return "To-Do List API. Используйте /tasks, /add_task, /complete_task"
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks})
@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({"error": "Задача не найдена"}), 404
@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        new_task = {
            "id": max(t["id"] for t in tasks) + 1 if tasks else 1,
            "task": request.json["task"],
            "done": False
        }
        tasks.append(new_task)
        return jsonify({"message": "Задача добавлена", "task": new_task}), 201
    except:
        return jsonify({"error": "Неверные данные"}), 400
@app.route('/complete_task/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task:
        task["done"] = True
        return jsonify({"message": "Задача выполнена", "task": task})
    return jsonify({"error": "Задача не найдена"}), 404
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
