from sqlalchemy import func, case
from bdmodels import session, Student, Grade, Course, Teacher, Group, Obshaga, Room, Schedule, Auditories, Comissions

print("1. Успеваемость студента")
results = session.query(Student.name, Course.title, Grade.score, Teacher.teacher_name).join(Grade, Student.student_id == Grade.student_id).join(Course, Grade.course_id == Course.course_id).join(Teacher, Course.teacher_id == Teacher.teacher_id).filter(Student.name == 'Студентов А.А.').all()
for r in results:
    print(r)

print("2. Студенты группы с общежитием")
results = session.query(Group.group_name, Student.name, Obshaga.name, Room.room_number).join(Student, Group.group_id == Student.group_name).outerjoin(Obshaga, Student.obshaga_name == Obshaga.obshaga_num).outerjoin(Room, Obshaga.obshaga_num == Room.obshaga_num).filter(Group.group_name == 'ИК-21').all()
for r in results:
    print(r)

print("3. Рейтинг групп")
avg_score = func.avg(Grade.score)
results = session.query(Group.group_name, func.count(Student.student_id), avg_score, case((avg_score >= 90, 'Отлично'), (avg_score >= 75, 'Хорошо'), else_='Нормально')).join(Student, Group.group_id == Student.group_name).outerjoin(Grade, Student.student_id == Grade.student_id).group_by(Group.group_id, Group.group_name).all()
for r in results:
    print(r)

print("4. Статистика преподавателей")
results = session.query(Teacher.teacher_name, func.count(func.distinct(Course.course_id)), func.sum(Course.credits), func.avg(Grade.score)).join(Course, Teacher.teacher_id == Course.teacher_id).outerjoin(Grade, Course.course_id == Grade.course_id).group_by(Teacher.teacher_id, Teacher.teacher_name).having(func.count(func.distinct(Course.course_id)) > 0).all()
for r in results:
    print(r)

print("5. Пересдачи")
results = session.query(Student.name, Course.title, Comissions.com_grade).join(Student, Comissions.student == Student.student_id).join(Course, Comissions.course == Course.course_id).filter(Comissions.com_grade < 3).all()
for r in results:
    print(r)

print("6. Расписание")
results = session.query(Schedule.day_of_week, Schedule.start_time, Course.title, Teacher.teacher_name, Auditories.audit).join(Course, Schedule.course_id == Course.course_id).join(Teacher, Schedule.teacher_id == Teacher.teacher_id).join(Auditories, Schedule.audit_name == Auditories.audit).filter(Schedule.group_id == 1).order_by(Schedule.day_of_week, Schedule.start_time).all()
for r in results:
    print(r)

session.close()