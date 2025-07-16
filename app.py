from flask import Flask, render_template, url_for, request, redirect, jsonify, make_response
from datetime import datetime
import uuid

app = Flask(__name__)

todo_status = 'Todo'
inprogress_status = 'In progress'
resolved_status = 'Resolved'

todos = []

class Todo:
    def __init__(self, name, content, status, date, id):
        self.name = name
        self.content = content
        self.status = status
        self.date = date
        self.id = id

    
    def __str__(self):
        return f"Todo(name='{self.name}', content={self.content}, status={self.status}, date={self.date}. id={self.id})"
    
    def to_dict(self):
        return {"name": self.name, "content": self.content, "status": self.status, "date": self.date, "id": self.id}



@app.route('/taskmanager', methods=['POST', 'GET'])
def task_manager():
    if request.method == 'POST':
        json = request.get_json()
        name = json.get('name')
        content = json.get('content')
        id = uuid.uuid4()
        todo = Todo(name, content, todo_status, datetime.today(), id)
        todos.append(todo)

        return jsonify(todo.to_dict()), 201
    
    else:
        todos_dict_format = []
        for todo in todos:
            todo_in_dict_format = todo.to_dict()
            todos_dict_format.append(todo_in_dict_format)
            for el in todos_dict_format:
                print(el)
                for i in el:
                    return jsonify(el.get("name"), el.get("id")), 200


if __name__ == "__main__":
    app.run(debug=True)