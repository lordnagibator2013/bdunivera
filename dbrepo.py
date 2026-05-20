import json
import redis
from bdmodels import session, Student, Group, Department, Course, Teacher, Grade
from sqlalchemy import func

redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)

class StudentRepository:
    @staticmethod
    def get_all():
        cached = redis_client.get('students:all')
        if cached:
            return json.loads(cached)
        
        students = session.query(Student).all()
        data = [{'id': s.student_id, 'name': s.name, 'group': s.group_name} for s in students]
        redis_client.setex('students:all', 300, json.dumps(data))
        return data
    
    @staticmethod
    def get_by_id(student_id):
        cached = redis_client.get(f'student:{student_id}')
        if cached:
            return json.loads(cached)
        
        student = session.query(Student).filter_by(student_id=student_id).first()
        if student:
            data = {'id': student.student_id, 'name': student.name, 'group': student.group_name}
            redis_client.setex(f'student:{student_id}', 300, json.dumps(data))
            return data
        return None
    
    @staticmethod
    def create(name, group_name):
        student = Student(name=name, group_name=group_name)
        session.add(student)
        session.commit()
        redis_client.delete('students:all')
        return student.student_id
    
    @staticmethod
    def update(student_id, name=None, group_name=None):
        student = session.query(Student).filter_by(student_id=student_id).first()
        if student:
            if name:
                student.name = name
            if group_name:
                student.group_name = group_name
            session.commit()
            redis_client.delete('students:all')
            redis_client.delete(f'student:{student_id}')
        return student
    
    @staticmethod
    def delete(student_id):
        student = session.query(Student).filter_by(student_id=student_id).first()
        if student:
            session.delete(student)
            session.commit()
            redis_client.delete('students:all')
            redis_client.delete(f'student:{student_id}')
        return student is not None

class GroupRepository:
    @staticmethod
    def get_all():
        cached = redis_client.get('groups:all')
        if cached:
            return json.loads(cached)
        
        groups = session.query(Group).all()
        data = [{'id': g.group_id, 'name': g.group_name, 'dept': g.department_id} for g in groups]
        redis_client.setex('groups:all', 300, json.dumps(data))
        return data
    
    @staticmethod
    def get_by_id(group_id):
        cached = redis_client.get(f'group:{group_id}')
        if cached:
            return json.loads(cached)
        
        group = session.query(Group).filter_by(group_id=group_id).first()
        if group:
            data = {'id': group.group_id, 'name': group.group_name, 'dept': group.department_id}
            redis_client.setex(f'group:{group_id}', 300, json.dumps(data))
            return data
        return None
    
    @staticmethod
    def get_with_avg_score(group_id):
        key = f'group:{group_id}:avg'
        cached = redis_client.get(key)
        if cached:
            return json.loads(cached)
        
        result = session.query(Group.group_name, func.avg(Grade.score)).join(Student).join(Grade).filter(Group.group_id == group_id).first()
        if result:
            data = {'name': result[0], 'avg_score': float(result[1]) if result[1] else 0}
            redis_client.setex(key, 300, json.dumps(data))
            return data
        return None

def invalidate_cache(pattern='*'):
    keys = redis_client.keys(pattern)
    if keys:
        redis_client.delete(*keys)