from flask import Flask, jsonify, request

app = Flask(__name__)  # __main__
app.config['SECRET_KEY'] = "secret1234"  # this key used to secert data coming from form

todo_list = [
    {'name': 'task_One', 'id': 0},
    {'name': 'task_Two', 'id': 1},
    {'name': 'task_Three', 'id': 2}
]


@app.route('/', methods=['GET'])
def hello_view():
    return jsonify({
        "todo_list": todo_list
    })


@app.route('/todo', methods=['GET', 'POST'])
def list_todo_list():
    if request.method == 'GET':
        return jsonify(todo_list)
    elif request.method == 'POST':
        print(request.form)
        task_name = request.form.get('task_name')
        task_id = request.form.get('task_id')

        todo_list.append(
            {'name': task_name, 'id': task_id}

        )
        return jsonify(todo_list)


@app.route('/todo/<int:task_id>', methods=['GET', 'DELETE'])
def todo_Retrive_Delete(task_id):
    if request.method == 'GET':
        return jsonify(todo_list[task_id])

    elif request.method == 'DELETE':
        del todo_list[task_id]
        return {'message': 'deleted task'}, 200


@app.route('/todo/<string:task_name>', methods=['GET'])
def todo_detail(task_name):
    try:
        print(task_name)
        return jsonify(todo_list[1])
    except Exception as e:
        pass
    return "No task found"
