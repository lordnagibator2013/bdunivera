from sqlalchemy import create_engine, Column, Integer, String, Date, Time, ForeignKey, CheckConstraint
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "postgresql://postgres:sky@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Department(Base):
    __tablename__ = 'department'
    department_id = Column(Integer, primary_key=True)
    department_name = Column(String(90), nullable=False)
    department_head_name = Column(String(90))
    groups = relationship('Group', back_populates='department')
    teachers = relationship('Teacher', back_populates='department')

class Group(Base):
    __tablename__ = 'groups'
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(20), unique=True)
    department_id = Column(Integer, ForeignKey('department.department_id'))
    department = relationship('Department', back_populates='groups')
    students = relationship('Student', back_populates='group')

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    group_name = Column(Integer, ForeignKey('groups.group_id'))
    obshaga_name = Column(Integer, ForeignKey('obshaga.obshaga_num'))
    enrolled_date = Column(Date)
    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')

class Teacher(Base):
    __tablename__ = 'teachers'
    teacher_id = Column(Integer, primary_key=True)
    teacher_name = Column(String(100), nullable=False)
    department_id = Column(Integer, ForeignKey('department.department_id'))
    department = relationship('Department', back_populates='teachers')
    courses = relationship('Course', back_populates='teacher')

class Course(Base):
    __tablename__ = 'courses'
    __table_args__ = (CheckConstraint('credits > 0'),)
    course_id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))
    title = Column(String(150), unique=True, nullable=False)
    credits = Column(Integer)
    teacher = relationship('Teacher', back_populates='courses')
    grades = relationship('Grade', back_populates='course')

class Grade(Base):
    __tablename__ = 'grades'
    __table_args__ = (CheckConstraint('score BETWEEN 0 AND 100'),)
    grade_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.student_id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    score = Column(Integer)
    graded_date = Column(Date)
    student = relationship('Student', back_populates='grades')
    course = relationship('Course', back_populates='grades')

class Obshaga(Base):
    __tablename__ = 'obshaga'
    obshaga_num = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True)

class Room(Base):
    __tablename__ = 'room'
    room_num = Column(Integer, primary_key=True)
    obshaga_num = Column(Integer, ForeignKey('obshaga.obshaga_num'))
    room_number = Column(String(10), nullable=False)

class Staff(Base):
    __tablename__ = 'staff'
    staff_id = Column(Integer, primary_key=True)
    staff_type = Column(String(20))
    staff_placement = Column(Integer, ForeignKey('obshaga.obshaga_num'))

class Comissions(Base):
    __tablename__ = 'comissions'
    com_id = Column(Integer, primary_key=True)
    com_date = Column(Date)
    com_grade = Column(Integer)
    course = Column(Integer, ForeignKey('courses.course_id'))
    student = Column(Integer, ForeignKey('students.student_id'))

class Auditories(Base):
    __tablename__ = 'auditories'
    audit = Column(String(10), primary_key=True)

class Schedule(Base):
    __tablename__ = 'schedule'
    __table_args__ = (CheckConstraint('day_of_week BETWEEN 1 AND 6'),)
    schedule_id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('groups.group_id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))
    audit_name = Column(String(10), ForeignKey('auditories.audit'))
    day_of_week = Column(Integer)
    start_time = Column(Time)
    
    group = relationship('Group')
    course = relationship('Course')
    teacher = relationship('Teacher')

Base.metadata.create_all(engine)
print("ww")