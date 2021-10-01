from functools import wraps
from flask import jsonify
from flask_jwt import current_identity


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if current_identity.is_admin:
            return fn(*args, **kwargs)
        return jsonify({'error':"Forbidden: you don't have permission to access this resource!"}), 403
    return wrapper


def is_self_or_admin(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if current_identity.is_admin or current_identity.id == kwargs.get('id'):
            return fn(*args, **kwargs)
        return jsonify({'error':"Forbidden: you don't have permission to access this resource!"}), 403
    return wrapper
