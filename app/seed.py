from app.models import UserModel


def user_seed(session):
    session.add(UserModel(username="FirstUser"))
    session.add(UserModel(username="SecondUser"))
    session.commit()
