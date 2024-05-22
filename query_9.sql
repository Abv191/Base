-- query_9.sql
SELECT subjects.name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
WHERE grades.student_id = 1; -- замініть на потрібний ID студента
