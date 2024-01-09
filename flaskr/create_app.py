from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    from flaskr.model import db
    migrate = Migrate(app, db)
    db.init_app(app)
    CORS(app)
    from flaskr.views.admin import admin
    from flaskr.views.frontend import frontend
    from flaskr.api.upload import upload_api
    app.register_blueprint(admin)
    app.register_blueprint(frontend)
    app.register_blueprint(upload_api)
    return app
