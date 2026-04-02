from flask_restful import abort, Resource, reqparse
from flask import jsonify

from data import db_session
from data.user import User


def abort_if_users_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"News {users_id} not found")


parser = reqparse.RequestParser()
parser.add_argument("surname", required=True)
parser.add_argument("name", required=True)
parser.add_argument("age", required=True, type=int)
parser.add_argument("position", required=True)
parser.add_argument("speciality", required=True)
parser.add_argument("address", required=True)
parser.add_argument("email", required=True)
parser.add_argument("modified_date", required=True)


class UsersResource(Resource):
    def get(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        return jsonify(users.to_dict(only=(
            "id", "surname", "name", "age", "position", "speciality", "address",
            "email", "modified_date"
        )))

    def delete(self, users_id):
        abort_if_users_not_found(users_id)
        session = db_session.create_session()
        users = session.query(User).get(users_id)
        session.delete(users)
        session.commit()
        return jsonify({"success": "ok"})

    def put(self, users_id):
        abort_if_users_not_found(users_id)
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            id=users_id,
            surname=args["surname"],
            name=args["name"],
            age=args["age"],
            position=args["position"],
            speciality=args["speciality"],
            address=args["address"],
            email=args["email"],
            modified_date=args["modified_date"]
        )
        session.merge(users)
        session.commit()
        return jsonify(users.to_dict(only=(
            "id", "surname", "name", "age", "position", "speciality", "address",
            "email", "modified_date"
        )))


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({
            "users": [
                user.to_dict(only=(
                    "id", "surname", "name", "age", "position", "speciality", "address",
                    "email", "modified_date")
                ) for user in users
            ]
        })

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        users = User(
            surname=args["surname"],
            name=args["name"],
            age=args["age"],
            position=args["position"],
            speciality=args["speciality"],
            address=args["address"],
            email=args["email"],
            modified_date=args["modified_date"]
        )
        session.add(users)
        session.commit()
        return jsonify({"id": users.id})
