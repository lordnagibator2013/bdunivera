create table obshaga(
	obshaga_num serial primary key,
	name varchar(30) unique
);

create table room(
	room_num serial primary key,
	obshaga_num int references obshaga(obshaga_num),
	room_number VARCHAR(10) NOT NULL
);

create table staff(
	staff_id serial primary key,
	staff_type varchar(20),
	staff_placement int references obshaga(obshaga_num)
);


create table department (
	department_id SERIAL primary key,
	department_name VARCHAR(90) not null,
	department_head_name VARCHAR(90)
);

create table groups (
	group_id serial primary key,
	group_name varchar(20) unique,
	department_id int references department(department_id)
);

CREATE TABLE teachers (
	teacher_id SERIAL PRIMARY KEY,
	teacher_name varchar(100) not null,
	department_id int references department(department_id)
);

CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(100) unique NOT NULL,
    group_name int references groups(group_id),
    obshaga_name int references obshaga(obshaga_num),
    enrolled_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    teacher_id INT references teachers(teacher_id),
    title VARCHAR(150) unique NOT NULL,
    credits INT CHECK (credits > 0)
);

CREATE TABLE grades (
    grade_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES students(student_id),
    course_id INT REFERENCES courses(course_id),
    score INT CHECK (score BETWEEN 0 AND 100),
    graded_date DATE DEFAULT CURRENT_DATE
);


create table comissions (
	com_id serial primary key,
	com_date DATE DEFAULT CURRENT_DATE,
	com_grade int,
	course int references courses(course_id),
	student int references students(student_id)
);

create table auditories (
	audit varchar(10) primary key
);

CREATE TABLE schedule (
    schedule_id SERIAL PRIMARY KEY,
    group_id INT REFERENCES groups(group_id),
    course_id INT REFERENCES courses(course_id),
    teacher_id INT REFERENCES teachers(teacher_id),
    audit_name varchar(10) REFERENCES auditories(audit),
    day_of_week INT CHECK (day_of_week BETWEEN 1 AND 6),
    start_time TIME
);

CREATE DATABASE dbname;

--DROP TABLE students, grades, courses, teachers, comissions, department, groups, obshaga, room, staff, auditories, schedule CASCADE;
