from data.db_session import global_init, create_session
from data.user import User

global_init(input())
session = create_session()

result = session.query(User).filter(
    User.address == "module_1",
    User.speciality.not_like("%engineer%"),
    User.position.not_like("%engineer%")
).all()

for user in result:
    print(user.id)
