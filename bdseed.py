from sqlalchemy import text
from bdmodels import session, Department, Group, Teacher, Course, Student, Auditories, Schedule, Obshaga, Grade, Comissions, Room, Staff

session.execute(text("TRUNCATE TABLE department, groups, students, teachers, courses, grades, schedule, auditories, comissions, obshaga, room, staff RESTART IDENTITY CASCADE"))
session.commit()

obshagas = [
    Obshaga(obshaga_num=1, name='Общага 1'),
    Obshaga(obshaga_num=2, name='Общага 2')
]

departments = [
    Department(department_name='Кафедра ИТ', department_head_name='Иванов И.И.'),
    Department(department_name='Кафедра Экономики', department_head_name='Петров П.П.')
]

groups = [
    Group(group_name='ИК-21', department_id=1),
    Group(group_name='ИК-22', department_id=1),
    Group(group_name='ЭК-21', department_id=2)
]

teachers = [
    Teacher(teacher_name='Сидоров А.А.', department_id=1),
    Teacher(teacher_name='Кузнецова Б.Б.', department_id=1),
    Teacher(teacher_name='Смирнов В.В.', department_id=2)
]

courses = [
    Course(title='Базы данных', credits=4, teacher_id=1),
    Course(title='Программирование', credits=5, teacher_id=2),
    Course(title='Макроэкономика', credits=3, teacher_id=3)
]

students = [
    Student(name='Студентов А.А.', group_name=1, obshaga_name=1),
    Student(name='Студентова Б.Б.', group_name=1, obshaga_name=2),
    Student(name='Экономов В.В.', group_name=3, obshaga_name=None),
    Student(name='Программистов Г.Г.', group_name=2, obshaga_name=1)
]

auditories = [
    Auditories(audit='101'),
    Auditories(audit='102'),
    Auditories(audit='205')
]

schedules = [
    Schedule(group_id=1, course_id=1, teacher_id=1, audit_name='101', day_of_week=1, start_time='08:30'),
    Schedule(group_id=1, course_id=2, teacher_id=2, audit_name='102', day_of_week=2, start_time='10:30'),
    Schedule(group_id=2, course_id=1, teacher_id=1, audit_name='101', day_of_week=1, start_time='10:30'),
    Schedule(group_id=3, course_id=3, teacher_id=3, audit_name='205', day_of_week=3, start_time='08:30')
]

grades = [
    Grade(student_id=1, course_id=1, score=85),
    Grade(student_id=1, course_id=2, score=90),
    Grade(student_id=2, course_id=1, score=70),
    Grade(student_id=3, course_id=3, score=60),
    Grade(student_id=4, course_id=1, score=95)
]

session.add_all(obshagas + departments + groups + teachers + courses + students + auditories + schedules + grades)
session.commit()

comissions = [
    Comissions(com_date='2024-01-15', com_grade=2, course=1, student=1),
    Comissions(com_date='2024-01-16', com_grade=3, course=1, student=2),
    Comissions(com_date='2024-01-17', com_grade=2, course=3, student=3)
]
session.add_all(comissions)
session.commit()

print("Done")