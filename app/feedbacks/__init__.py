from flask import Blueprint

bp = Blueprint("feedbacks", __name__)

from app.feedbacks import routes
