from flask import Flask, jsonify, request
from Model.cereal import cereal
from Model.Dataset import tasks
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


@app.route('/')
def hello_world():
  return "hello world"

@app.route('/get/task', methods = ['GET'])
def getData():
    """
    ini adalah Endpoint untuk mengambil seluruh data yang ada.
    ---
    tags:
        - Rest Controller
    parameter:
    responses:
        200:
            description: Success Get All Data
    """
    return jsonify({'tasks': tasks, 'success': True})

@app.route('/input/task', methods = ['POST'])
def inputTask():
    """
        ini adalah Endpoint untuk menginput data task.
        ---
        tags:
            - Rest Controller
        parameter:
            - name: body
                in: body
                required: true
                schema:
                    id: product
                    required:
                    - calories
                    - protein
                    - fat
                    - sodium
                    - fiber
                    - carbo
                    - potass
                    - vitamins
                properties:
                    calories:
                        type: int
                        description: input with valid data
                        default: 0
                    protein:
                        type: int
                        description: input with valid data
                        default: 0
                    fat:
                        type: int
                        description: input with valid data
                        default: 0
                    sodium:
                        type: int
                        description: input with valid data
                        default: 0
                    fiber:
                        type: int
                        description: input with valid data
                        default: 0
                    carbo:
                        type: int
                        description: input with valid data
                        default: 0
                    potass:
                        type: int
                        description: input with valid data
                        default: 0
                    vitamins:
                        type: int
                        description: input with valid data
                        default: 0
        responses:
            200:
                description: Success Input
        """
    newData = request.get_json()

    calories = newData['calories']
    protein = newData['protein']
    fat = newData['fat']
    sodium = newData['sodium']
    fiber = newData['fiber']
    carbo = newData['carbo']
    potass = newData['potass']
    vitamins = newData['vitamins']

    newcereal = cereal(calories,  protein,  fat,  sodium,  fiber,  carbo,  potass,  vitamins)

    tasks.append(newcereal.__dict__)

    return jsonify({'message': 'success'})

@app.route('/update/task/<int:id>', methods = ['PUT'])
def updateTask():
    """
            ini adalah Endpoint untuk menginput data task.
            ---
            tags:
                - Rest Controller
            parameter:
                - in: path
                    name: id
                    required: true
                    type: integer
                - in: body
                    name: body
                    required: true
                    schema:
                        id: cereal
                        required:
                        - calories
                        - protein
                        - fat
                        - sodium
                        - fiber
                        - carbo
                        - potass
                        - vitamins
                    properties:
                        calories:
                            type: int
                            description: input with valid data
                            default: 0
                        protein:
                            type: int
                            description: input with valid data
                            default: 0
                        fat:
                            type: int
                            description: input with valid data
                            default: 0
                        sodium:
                            type: int
                            description: input with valid data
                            default: 0
                        fiber:
                            type: int
                            description: input with valid data
                            default: 0
                        carbo:
                            type: int
                            description: input with valid data
                            default: 0
                        potass:
                            type: int
                            description: input with valid data
                            default: 0
                        vitamins:
                            type: int
                            description: input with valid data
                            default: 0
            responses:
                200:
                    description: Success Update
            """
    new_task = request.get_json()

    calories = new_task['calories']
    protein = new_task['protein']
    fat = new_task['fat']
    sodium = new_task['sodium']
    fiber = new_task['fiber']
    carbo = new_task['carbo']
    potass = new_task['potass']
    vitamins = new_task['vitamins']

    newcereal = cereal(calories,  protein,  fat,  sodium,  fiber,  carbo,  potass,  vitamins)

    tasks[id] = newcereal.__dict__

@app.route ('/delete/task/<int:id>' , methods = ['DELETE'])
def deleteTask (id):
    """
        ini adalah Endpoint untuk mengambil seluruh data yang ada.
        ---
        tags:
            - Rest Controller
        parameter:
            in: path
            name: id
            required: true
            type: integer
        responses:
            200:
                description: Success Delete
        """
    del tasks[id]

    return jsonify({'message': 'success delete'})

if __name__ == "__main__" :
    app.run(debug=True)