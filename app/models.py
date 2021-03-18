from app import db


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"


class FeedbackModel(db.Model):
    __tablename__ = "feedbacks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(36), nullable=False)
    data = db.Column(db.String(1000), nullable=False)
    challenge_id = db.Column(db.String(36), nullable=True)

    def __repr__(self):
        return f"<Feedback(id={self.id}, data={self.data}, user_id={self.user_id}, challenge_id={self.challenge_id})>"
