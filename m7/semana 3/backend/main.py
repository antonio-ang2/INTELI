from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from models import User, Note
app = Flask(__name__)

DATABASE_URL = "postgresql://postgres:senha@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Rotas para a tabela "users"

@app.route('/users', methods=['GET'])
def get_users():
    session = Session()
    users = session.query(User).all()
    user_list = [{'id': user.id, 'username': user.username, 'password': user.password} for user in users]
    session.close()
    return jsonify(user_list)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    session = Session()
    user = session.query(User).get(user_id)
    session.close()
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'password': user.password})
    return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    session = Session()

    try:
        user = User(username=data['username'], password=data['password'])
        session.add(user)
        session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    session = Session()

    try:
        user = session.query(User).get(user_id)
        if user:
            user.username = data['username']
            user.password = data['password']
            session.commit()
            return jsonify({'message': 'User updated successfully'}), 200
        return jsonify({'message': 'User not found'}), 404
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    session = Session()

    try:
        user = session.query(User).get(user_id)
        if user:
            session.delete(user)
            session.commit()
            return jsonify({'message': 'User deleted successfully'}), 200
        return jsonify({'message': 'User not found'}), 404
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

# Rotas para a tabela "grades"

@app.route('/grades', methods=['GET'])
def get_grades():
    session = Session()
    grades = session.query(Note).all()
    grade_list = [{'id': grade.id, 'grade': grade.grade, 'user_id': grade.user_id} for grade in grades]
    session.close()
    return jsonify(grade_list)

@app.route('/grades/<int:grade_id>', methods=['GET'])
def get_grade(grade_id):
    session = Session()
    grade = session.query(Note).get(grade_id)
    session.close()
    if grade:
        return jsonify({'id': grade.id, 'grade': grade.grade, 'user_id': grade.user_id})
    return jsonify({'message': 'Grade not found'}), 404

@app.route('/grades', methods=['POST'])
def create_grade():
    data = request.json
    session = Session()

    try:
        grade = Note(grade=data['grade'], user_id=data['user_id'])
        session.add(grade)
        session.commit()
        return jsonify({'message': 'Grade created successfully'}), 201
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/grades/<int:grade_id>', methods=['PUT'])
def update_grade(grade_id):
    data = request.json
    session = Session()

    try:
        grade = session.query(Note).get(grade_id)
        if grade:
            grade.grade = data['grade']
            grade.user_id = data['user_id']
            session.commit()
            return jsonify({'message': 'Grade updated successfully'}), 200
        return jsonify({'message': 'Grade not found'}), 404
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

@app.route('/grades/<int:grade_id>', methods=['DELETE'])
def delete_grade(grade_id):
    session = Session()

    try:
        grade = session.query(Note).get(grade_id)
        if grade:
            session.delete(grade)
            session.commit()
            return jsonify({'message': 'Grade deleted successfully'}), 200
        return jsonify({'message': 'Grade not found'}), 404
    except SQLAlchemyError as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)
