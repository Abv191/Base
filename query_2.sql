-- query_2.sql
SELECT students.name, AVG(grades.grade) as average_grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = 1 -- замініть на потрібний ID предмета
GROUP BY students.id
ORDER BY average_grade DESC
LIMIT 1;
