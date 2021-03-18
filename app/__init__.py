from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy

from app.errors import InternalError, NotFoundError
from config import Config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.errorhandler(404)
    def not_found_error(error):
        return NotFoundError().message

    @app.errorhandler(500)
    def internal_error(error):
        return InternalError().message

    with app.test_request_context():
        db.init_app(app)
        db.create_all()

        from app.seed import user_seed

        user_seed(db.session)

    @app.before_request
    def setup_db_session():
        g.db_session = db.session

    from app.feedbacks import bp as feedbacks_bp

    app.register_blueprint(feedbacks_bp, url_prefix="/feedbacks")

    return app


from app import models
