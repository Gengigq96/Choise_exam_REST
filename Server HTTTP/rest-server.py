#!flask/bin/python3
from flask import Flask, request
from flask_restful import Resource, Api
import json
app = Flask(__name__)
api = Api(app)


x = {"exam": {  
  "id": "1",    
  "Questions": {  
    "1": [
  	  {"Question": "1+1="},
      {"value": "2"},  
      {"value": "1"},  
      {"value": "3"}  
    ],
    "2": [
  	  {"Question": "1+3="},
      {"value": "2"},  
      {"value": "1"},  
      {"value": "4"}  
    ],
    "3": [
  	  {"Question": "1+3="},
      {"value": "2"},  
      {"value": "1"},  
      {"value": "4"}  
    ]
  }  
}}
y = {"exam": {  
  "id": "2",    
  "Questions": {  
    "1": [
  	  {"Question": "23+1="},
      {"value": "24"},  
      {"value": "1"},  
      {"value": "3"}  
    ],
    "2": [
  	  {"Question": "7+3="},
      {"value": "10"},  
      {"value": "1"},  
      {"value": "4"}  
    ],
    "3": [
  	  {"Question": "1+3="},
      {"value": "4"},  
      {"value": "1"},  
      {"value": "2"}  
    ]
  }  
}}
z = {"exam": {  
  "id": "3",    
  "Questions": {  
    "1": [
  	  {"Question": "23+7="},
      {"value": "30"},  
      {"value": "1"},  
      {"value": "3"}  
    ],
    "2": [
  	  {"Question": "7+9="},
      {"value": "16"},  
      {"value": "1"},  
      {"value": "4"}  
    ],
    "3": [
  	  {"Question": "1+0="},
      {"value": "4"},  
      {"value": "1"},  
      {"value": "2"}  
    ]
  }  
}}

examen1 = json.dumps(x) 
examen2 = json.dumps(y)
examen3 = json.dumps(z)
exams = {1:examen1,2:examen2,3:examen3}

class Index(Resource):
    def get(self):
        return json.dumps(x)
    def post(self):
        some_json = request.get_json()
        return {'You sent ': some_json}, 201

class Exams(Resource):
    def get(slef, num):
        return (exams.get(num))

api.add_resource(Index, '/')
api.add_resource(Exams, '/exams/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)

