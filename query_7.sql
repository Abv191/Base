-- query_7.sql
SELECT students.name, grades.grade, grades.date
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = 1 -- замініть на потрібний ID групи
AND grades.subject_id = 1; -- замініть на потрібний ID предмета
