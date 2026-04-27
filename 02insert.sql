--DROP TABLE IF EXISTS students, grades, courses, teachers, comissions, department, groups, obshaga, room, staff CASCADE;

INSERT INTO department (department_id, department_name, department_head_name) VALUES
(1, 'Кафедра ИТ', 'Иванов И.И.'),
(2, 'Кафедра Экономики', 'Петров П.П.');

INSERT INTO obshaga (obshaga_num, name) VALUES
(1, 'Общага №1'),
(2, 'Общага №2');

INSERT INTO groups (group_id, group_name, department_id) VALUES
(1, 'ИК-21', 1),
(2, 'ЭК-22', 2);

INSERT INTO teachers (teacher_id, teacher_name, department_id) VALUES
(1, 'Сидоров А.А.', 1),
(2, 'Кузнецова Б.Б.', 2);

INSERT INTO room (room_num, obshaga_num, room_number) VALUES
(1, 1, '101'),
(2, 1, '102'),
(3, 2, '205');

INSERT INTO staff (staff_id, staff_type, staff_placement) VALUES
(1, 'Комендант', 1),
(2, 'Охранник', 2);

INSERT INTO students (student_id, name, group_name, obshaga_name, enrolled_date) VALUES
(1, 'Студентов А.А.', 1, 1, '2023-09-01'),
(2, 'Студентова Б.Б.', 1, 2, '2023-09-01'),
(3, 'Экономов В.В.', 2, NULL, '2023-09-01');

INSERT INTO courses (course_id, teacher_id, title, credits) VALUES
(1, 1, 'Базы данных', 4),
(2, 1, 'Программирование', 5),
(3, 2, 'Танцы с чебупиццей', 3);

INSERT INTO grades (student_id, course_id, score, graded_date) VALUES
(1, 1, 85, '2023-12-01'),
(1, 2, 90, '2023-12-01'),
(2, 1, 70, '2023-12-01'),
(3, 3, 80, '2023-12-01');

INSERT INTO comissions (com_id, com_date, com_grade, course, student) VALUES
(1, '2024-01-15', 4, 1, 1),
(2, '2024-01-15', 5, 2, 1);

INSERT INTO auditories (audit) VALUES
('A101'),
('A102'),
('A205');

INSERT INTO schedule (group_id, course_id, teacher_id, audit_name, day_of_week, start_time) VALUES
(1, 1, 1, 'A101', 1, '10:00'),
(1, 2, 1, 'A102', 2, '11:40'),
(1, 1, 1, 'A101', 3, '13:20');