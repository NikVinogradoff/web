from sqlalchemy import Column, Integer, String, ForeignKey, orm

from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True, unique=True)
    title = Column(String)
    chief = Column(Integer)
    members = Column(Integer, ForeignKey("users.id"))
    member = orm.relationship("User")
    email = Column(String)
