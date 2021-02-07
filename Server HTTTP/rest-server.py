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

    def post(self, id_exam):

        data = request.get_json()

        cursor_modify_desc_exam = mydb.cursor(dictionary=True)

        sql = "UPDATE exam SET description = '"+(data["description"])+"' WHERE id_exam = "+id_exam+";"


        cursor_modify_desc_exam.execute(sql)

        mydb.commit()

        debug_modify_desc_exam = str(cursor_modify_desc_exam.rowcount) + " record updated"

        return debug_modify_desc_exam, 201

    def delete(self, id_exam):


        cursor_delete_exam = mydb.cursor(dictionary=True)

        cursor_delete_exam.execute("DELETE FROM question WHERE id_exam = "+id_exam+"; ")

        debug_delete_question = cursor_delete_exam.rowcount

        cursor_delete_exam.execute("DELETE FROM exam WHERE id_exam = "+id_exam+";")

        mydb.commit()

        debug_delete_exam = str(cursor_delete_exam.rowcount + debug_delete_question) + " record(s) deleted"

        cursor_delete_exam.close()

        return debug_delete_exam, 201

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


# class ExamByDesc(Resource):
#
#     def get(self, txtSearch):
#
#         cursor_search_exam = mydb.cursor(dictionary=True)
#
#         cursor_search_exam.execute("SELECT * FROM exam WHERE description = \"*"+txtSearch+"*\";")
#
#         result_exams = cursor_search_exam.fetchall()
#
#         return (result_exams)


#LIST ALL EXAMS (GET) // POST AN EXAM (POST)
api.add_resource(Exams, '/exams/')
#LIST AN SPECIFIC EXAM (GET) // MODIFY DESC EXAM (POST) // DELETE EXAM (DELETE)
api.add_resource(Exam, '/exams/<string:id_exam>')
#POST A QUESTION OF AN SPECIFIC EXAM (POST)
api.add_resource(Question, '/question/<int:id_exam>')
#SEARCH EXAM BY FULL/PARTIAL DESC (GET)
#api.add_resource(ExamByDesc, '/exams/<string:txtSearch>')

#******
#SEARCH EXAM BY FULL/PARTIAL DESC (GET)
# api.add_resource(SearchExam, '/exams/<string:desc>')
# #UPLOAD (POST) AND DOWNLOAD (GET) STUDENTS GRADES
# api.add_resource(Grades, '/grades/<string:id_exam>')
# #MANAGE STUDENTS (GET)
# api.add_resource(Student, '/students/<string:id_student>')
#******


if __name__ == '__main__':
    app.run(debug=True)
