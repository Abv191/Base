import mysql.connector
from faker import Faker
import random

conn = mysql.connector.connect(
    host='localhost',
    user='yourusername',
    password='yourpassword',
    database='university'
)
cursor = conn.cursor()

faker = Faker()

group_names = ["Group A", "Group B", "Group C"]
for name in group_names:
    cursor.execute("INSERT INTO groups (name) VALUES (%s)", (name,))

teachers = [faker.name() for _ in range(5)]
for teacher in teachers:
    cursor.execute("INSERT INTO teachers (name) VALUES (%s)", (teacher,))

subject_names = ["Math", "History", "Physics", "Chemistry", "Biology", "Literature", "Art", "Computer Science"]
for name in subject_names:
    teacher_id = random.randint(1, len(teachers))
    cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (%s, %s)", (name, teacher_id))

for _ in range(50):
    name = faker.name()
    group_id = random.randint(1, len(group_names))
    cursor.execute("INSERT INTO students (name, group_id) VALUES (%s, %s)", (name, group_id))

for _ in range(1000):
    student_id = random.randint(1, 50)
    subject_id = random.randint(1, len(subject_names))
    grade = random.randint(1, 10)
    date = faker.date_this_year()
    cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (%s, %s, %s, %s)", (student_id, subject_id, grade, date))

conn.commit()

cursor.close()
conn.close()
