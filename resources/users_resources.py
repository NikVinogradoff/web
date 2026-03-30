from flask_restful import abort, Resource
from flask import jsonify

from data import db_session
from data.user import User


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"News {users_id} not found")


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify(users.to_dict(only=(
            "id", "surname", "name", "age", "position", "speciality", "address",
            "email", "hashed_password", "modified_date"
        )))

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({"success": "ok"})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({
            "jobs": [
                user.to_dict(only=(
                    "id", "surname", "name", "age", "position", "speciality", "address",
                    "email", "hashed_password", "modified_date")
                ) for user in users
            ]
        })
