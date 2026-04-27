SELECT 
    s.name AS student_name,
    c.title AS course_name,
    g.score,
    g.graded_date,
    t.teacher_name
FROM students s
JOIN grades g ON s.student_id = g.student_id
JOIN courses c ON g.course_id = c.course_id
JOIN teachers t ON c.teacher_id = t.teacher_id
WHERE s.name = 'Студентов А.А.'
ORDER BY g.graded_date DESC;

SELECT 
    g.group_name,
    s.name AS student_name,
    s.enrolled_date,
    o.name AS obshaga_name,
    r.room_number
FROM students s
JOIN groups g ON s.group_name = g.group_id
LEFT JOIN obshaga o ON s.obshaga_name = o.obshaga_num
LEFT JOIN room r ON o.obshaga_num = r.obshaga_num
WHERE g.group_name = 'ИК-21'
ORDER BY s.name;

SELECT 
    g.group_name,
    d.department_name,
    COUNT(DISTINCT s.student_id) AS students_count,
    ROUND(AVG(gr.score), 2) AS avg_score,
    CASE 
        WHEN AVG(gr.score) >= 90 THEN 'Отлично'
        WHEN AVG(gr.score) >= 75 THEN 'Хорошо'
        WHEN AVG(gr.score) >= 60 THEN 'Удовлетворительно'
        ELSE 'Плохо'
    END AS performance_level
FROM groups g
JOIN department d ON g.department_id = d.department_id
LEFT JOIN students s ON g.group_id = s.group_name
LEFT JOIN grades gr ON s.student_id = gr.student_id
GROUP BY g.group_id, g.group_name, d.department_name
ORDER BY avg_score DESC;

SELECT 
    d.department_name,
    d.department_head_name,
    COUNT(DISTINCT s.student_id) AS total_students,
    COUNT(DISTINCT gr.grade_id) AS total_grades,
    ROUND(AVG(gr.score), 2) AS avg_department_score,
    MIN(gr.score) AS min_score,
    MAX(gr.score) AS max_score
FROM department d
JOIN groups g ON d.department_id = g.department_id
JOIN students s ON g.group_id = s.group_name
JOIN grades gr ON s.student_id = gr.student_id
GROUP BY d.department_id, d.department_name, d.department_head_name
ORDER BY avg_department_score DESC;

SELECT 
    t.teacher_name,
    d.department_name,
    c.title AS course_title,
    c.credits,
    COUNT(DISTINCT gr.student_id) AS enrolled_students
FROM teachers t
JOIN department d ON t.department_id = d.department_id
JOIN courses c ON t.teacher_id = c.teacher_id
LEFT JOIN grades gr ON c.course_id = gr.course_id
GROUP BY t.teacher_id, t.teacher_name, d.department_name, c.course_id, c.title, c.credits
ORDER BY t.teacher_name, c.title;

SELECT 
    t.teacher_name,
    d.department_name,
    COUNT(DISTINCT c.course_id) AS courses_count,
    SUM(c.credits) AS total_credits,
    COUNT(DISTINCT gr.student_id) AS total_students,
    ROUND(AVG(gr.score), 2) AS avg_student_score
FROM teachers t
JOIN department d ON t.department_id = d.department_id
LEFT JOIN courses c ON t.teacher_id = c.teacher_id
LEFT JOIN grades gr ON c.course_id = gr.course_id
GROUP BY t.teacher_id, t.teacher_name, d.department_name
HAVING COUNT(DISTINCT c.course_id) > 0
ORDER BY total_credits DESC, courses_count DESC;

SELECT 
    s.name AS student_name,
    g.group_name,
    c.title AS course_name,
    com.com_grade,
    com.com_date,
    t.teacher_name AS course_teacher
FROM comissions com
JOIN students s ON com.student = s.student_id
JOIN courses c ON com.course = c.course_id
JOIN groups g ON s.group_name = g.group_id
JOIN teachers t ON c.teacher_id = t.teacher_id
WHERE com.com_grade < 3
ORDER BY com.com_date, s.name;

SELECT 
    s.day_of_week,
    s.start_time,
    c.title,
    t.teacher_name,
    a.audit
FROM schedule s
JOIN courses c ON s.course_id = c.course_id
JOIN teachers t ON s.teacher_id = t.teacher_id
JOIN auditories a ON s.audit_name = a.audit
WHERE s.group_id = 1
ORDER BY s.day_of_week, s.start_time;