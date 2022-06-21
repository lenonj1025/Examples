from flask import Flask, request

app = Flask(__name__)


users = {
    "lenonj1025": {
        "mobile_phone": "518-307-0001",
        "todos": [
            {
                "description": "Do laundry",
                "completed": False
            },
            {
                "description": "Take out trash",
                "completed": True
            },
            {
                "description": "Go to the doctor's office",
                "completed": False
            },
            {
                "description": "Wash dishes",
                "completed": True
            }
        ]
     },
    "jane12345": {
        "mobile_phone": "518-793-0002",
        "todos": []
    }
}

# Decorator
# Decorators are a concept from Python
# The @app.route decorator is coming from Flask
# And it is treating a function as the initial execution point
# whenever an HTTP request is received to that particular endpoint
@app.route('/test')
def hello():
    print("Hi, the hello() function is being executed")
    return "Hello World"


@app.route('/users')
def get_all_user():
    my_users = []
    for key in users:
        user = {
            "username": key,
            "mobile_phone": users[key]['mobile_phone'],
            "todos": users[key]['todos']
        }

        my_users.append(user)

    return {
            "users": my_users
    }, 200


# If a user with username X exists, return their information
# If a user with username X does not exist, return an error message and a 404 Not found status code
@app.route("/users/<username>")
def get_user_by_name(username):
    if username in users:
        return {
            "username": username,
            "mobile_phone": users[username]['mobile_phone'],
            "todos": users[username]['todos']
        }
    else:
        return{
            "message": f"User with username {username} does not exist"
        }, 404

@app.route('/users', methods=['POST'])
def create_user():
    # method that returns a dictionary representing the request body JSON
    data = request.get_json()

    if data['username'] in users:
        return {
            "message": f"User with username {data['username']} already exists. Cannot create a new user"
        }, 400
    else:
        return{
            "username": data['username'],
            "mobile_phone": users[data['username']]['mobile_phone'],
            "todos": users[data['username']['todos']]
        }, 201


@app.route('/user/<username>/todos')
def get_all_todos_by_user(username):
    # Check if user actually exists
    if username not in users:
        return{
            "message": f"User with username {username} that you are trying to retrieve todos from does not exist"
        }, 404
    # Check if completed query parameter is being used or not
    if request.args.get("completed"):
        if request.args.get("completed") == 'yes':
            # return the todos that are completed for that user
            completed_todos = []
            for todo in users[username]['todos']:
                if todo['completed']:
                    completed_todos.append(todo)
            return {
                "todos": completed_todos
            }, 200

        elif request.args.get("completed") == 'no':
            uncompleted_todos = []
            for todo in users[username]['todos']:
                if not todo['completed']:
                    uncompleted_todos.append(todo)
            return{
                "todos": uncompleted_todos
            }, 200

    return{
        "todos": users[username]['todos']
    }, 200


@app.route('/users/<username>/todos', methods=['POST'])
def create_todo(username):
    if username not in users:
        return{
            "message": f"User with username {username} that you are trying to add todo for does not exist"
        }, 404
    json = request.get_json()

    if str(json['description']).strip() == '':
        return {
            "message": "Description for todo cannot be blank"
        }, 400

    new_todo = {
        "description": json['description'],
        "completed": = False
    }

    users[username]['todos'].append(new_todo)

    return new_todo, 200


app.run(port=8080)
