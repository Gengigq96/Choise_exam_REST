#!flask/bin/python3
from flask import Flask, request
from flask_restful import Resource, Api
import mysql.connector
import json
import csv
import sys

app = Flask(__name__)
api = Api(app)

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="Admin_1234",
  database="exams"
)



class Exams(Resource):
    def get(self):

        cursor_exam = mydb.cursor(dictionary=True)

        cursor_exam.execute("SELECT * FROM exam")

        allexams = cursor_exam.fetchall()

        return (allexams)

    def post(self):

        data = request.get_json()

        cursor_store_exam = mydb.cursor(dictionary=True)

        sql = "INSERT INTO exam (description, date, time, location) VALUES (%s, %s, %s, %s)"
        values = (data["description"], data["date"], data["time"], data["location"])

        cursor_store_exam.execute(sql, values)

        mydb.commit()

        debug_store_exam = str(cursor_store_exam.rowcount) + " record inserted"

        return debug_store_exam, 201


class Exam(Resource):
    #def get(self):

    def get(self, id_exam):

        cursor_exam = mydb.cursor(dictionary=True)

        cursor_exam.execute("SELECT * FROM exam WHERE id_exam = "+id_exam+";")

        concrete_exam = cursor_exam.fetchall()

        return (concrete_exam)


class Question(Resource):

    def post(self, id_exam):

        data = request.get_json()

        cursor_store_exam = mydb.cursor(dictionary=True)

        sql = "INSERT INTO question (id_exam, question, answer1, answer2, answer3, correct_answer) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (id_exam, data["question"], data["answer1"], data["answer2"], data["answer3"], data["correct_answer"])

        cursor_store_exam.execute(sql, values)

        mydb.commit()

        debug_store_exam = str(cursor_store_exam.rowcount) + " record inserted"

        return debug_store_exam, 201



api.add_resource(Exams, '/exams/')
api.add_resource(Exam, '/exams/<string:id_exam>')
api.add_resource(Question, '/question/<int:id_exam>')


if __name__ == '__main__':
    app.run(debug=True)
