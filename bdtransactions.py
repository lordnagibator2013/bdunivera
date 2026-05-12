from sqlalchemy import text
from bdmodels import session, Student, Grade, Course, Group, Department, Teacher

def transfer_student():
    """Перевод студента в другую группу"""
    try:
        student = session.query(Student).filter_by(name='Студентов А.А.').first()
        old_group = student.group_name
        student.group_name = 2
        session.commit()
        print(f"Студент переведён из {old_group} в {student.group_name}")
    except Exception as e:
        session.rollback()
        print(f"Ошибка: {e}")

def add_grade_with_check():
    """Добавление оценки с проверкой диапазона"""
    try:
        grade = Grade(student_id=1, course_id=1, score=105)
        if grade.score < 0 or grade.score > 100:
            raise ValueError("Оценка должна быть 0-100")
        session.add(grade)
        session.commit()
        print("Оценка добавлена")
    except Exception as e:
        session.rollback()
        print(f"Откат: {e}")

def create_department_with_group():
    """Создание кафедры и группы"""
    try:
        dept = Department(department_name='Кафедра Физики', department_head_name='Ньютов И.И.')
        session.add(dept)
        session.flush()
        group = Group(group_name='ФИ-21', department_id=dept.department_id)
        session.add(group)
        session.commit()
        print("Кафедра и группа созданы")
    except Exception as e:
        session.rollback()
        print(f"Откат: {e}")

def delete_student_with_grades():
    """Удаление студента и его оценок"""
    try:
        student = session.query(Student).filter_by(name='Студентова Б.Б.').first()
        session.query(Grade).filter_by(student_id=student.student_id).delete()
        session.delete(student)
        session.commit()
        print("Студент и оценки удалены")
    except Exception as e:
        session.rollback()
        print(f"Откат: {e}")

def update_teacher_workload():
    """Изменение нагрузки преподавателя"""
    try:
        teacher = session.query(Teacher).filter_by(teacher_name='Сидоров А.А.').first()
        old_courses = session.query(Course).filter_by(teacher_id=teacher.teacher_id).count()
        new_course = Course(title='Новый курс', credits=3, teacher_id=teacher.teacher_id)
        session.add(new_course)
        session.commit()
        print(f"Курсов было: {old_courses}, стало: {old_courses + 1}")
    except Exception as e:
        session.rollback()
        print(f"Откат: {e}")

if __name__ == '__main__':
    print("1. Перевод студента")
    transfer_student()
    print("\n2. Добавление оценки")
    add_grade_with_check()
    print("\n3. Создание кафедры с группой")
    create_department_with_group()
    print("\n4. Удаление студента")
    delete_student_with_grades()
    print("\n5. Нагрузка преподавателя")
    update_teacher_workload()