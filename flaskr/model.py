from flask_sqlalchemy import SQLAlchemy
from flaskr import db
class Video(db.Model):
    file_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    video_path = db.Column(db.String(100),nullable=False)