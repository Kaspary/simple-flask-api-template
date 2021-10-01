from flask import jsonify, request, url_for, Response
from flask_jwt import jwt_required, current_identity
from user import app
from user.models import User
from user.decorators import admin_required, is_self_or_admin
from database import db_session


@app.route('', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    confirm_password = request.json.get('confirm_password')
    try:
        assert password == confirm_password, 'The passwords not match'
        user = User(username=username)
        user.set_password(password)
        db_session.add(user)
        db_session.commit()
    except AssertionError as e:
        return jsonify(error=str(e)), 400
    except Exception as e:
        Response(status=400)

    return jsonify({'location': url_for('user.retrive_user', id=user.id)}), 201


@app.route('/<int:id>', methods=['GET'])
@jwt_required()
@is_self_or_admin
def retrive_user(id):
    user = User.query.get(id)
    if not user:
        return Response(status=404)
    return jsonify(user)


@app.route('', methods=['GET'])
@jwt_required()
@admin_required
def list_user():
    users = User.query.all()
    if not users:
        Response(status=404)
    return jsonify({'data':users})


@app.route('/edit-password', methods=['POST'])
@jwt_required()
def edit_password():
    current_password = request.json.get('current_password')
    password = request.json.get('password')
    confirm_password = request.json.get('confirm_password')
    user = current_identity
    try:
        assert password == confirm_password, 'The passwords not match'
        if not user.check_password(current_password):
            return Response(status=401)
        user.set_password(password)
        db_session.commit()
    except AssertionError as e:
        return jsonify(error=str(e)), 400
    except Exception as e:
        Response(status=400)

    return Response(status=200)
