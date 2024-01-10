from flask_sqlalchemy import SQLAlchemy
# from flaskr import db
class Video:
    def __init__(self, title, video_path) -> None:
        self.title=title
        self.video_path=video_path