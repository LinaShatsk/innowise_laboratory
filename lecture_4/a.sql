--1 запрос
SELECT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE s.full_name = 'Alice Johnson'
ORDER BY g.subject; 

-- 2 запрос
SELECT s.full_name, AVG(g.grade) as average_grade
FROM students s
LEFT JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC; 

-- 3 запрос
SELECT id, full_name, birth_year
FROM students
WHERE birth_year > 2004
ORDER BY birth_year, full_name;

-- 4 запрос
SELECT subject, AVG(grade) as average_grade
FROM grades
GROUP BY subject
ORDER BY average_grade DESC; 

-- 5 запрос
SELECT s.full_name, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 3;

-- 6 запрос
SELECT DISTINCT s.full_name, g.subject, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.grade < 80
ORDER BY s.full_name, g.grade;