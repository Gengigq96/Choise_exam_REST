#!flask/bin/python3
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="Admin_1234",
  database="exams"
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS exam")
mycursor.execute("CREATE TABLE exam (id_exam INT AUTO_INCREMENT PRIMARY KEY, description VARCHAR(255), date VARCHAR(255),time VARCHAR(255),location VARCHAR(255))")
mycursor.execute("DROP TABLE IF EXISTS question")
mycursor.execute("CREATE TABLE question (id_question INT AUTO_INCREMENT, id_exam INT, question VARCHAR(255), answer1 VARCHAR(255),answer2 VARCHAR(255),answer3 VARCHAR(255), correct_answer VARCHAR(255),PRIMARY KEY (id_question, id_exam) ,CONSTRAINT fk_exam FOREIGN KEY (id_exam) REFERENCES exam(id_exam))")
mycursor.execute("DROP TABLE IF EXISTS student")
mycursor.execute("CREATE TABLE student (id_student VARCHAR(4) PRIMARY KEY)")
mycursor.execute("DROP TABLE IF EXISTS grade")
mycursor.execute("CREATE TABLE grade (id_student VARCHAR(4), id_exam INT, nota VARCHAR(255),CONSTRAINT fk_exam2 FOREIGN KEY (id_exam) REFERENCES exam(id_exam),PRIMARY KEY (id_student, id_exam),CONSTRAINT fk_student FOREIGN KEY (id_student) REFERENCES student(id_student))")


