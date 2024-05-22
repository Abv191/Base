-- query_3.sql
SELECT groups.name, AVG(grades.grade) as average_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = 1 -- замініть на потрібний ID предмета
GROUP BY groups.id;
