import os

from flask import Flask


def create_app(config_file):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    # initializes database
    from yourapplication.model import db
    db.init_app(app)
    # blueprint/modularization
    from yourapplication.views.admin import admin
    from yourapplication.views.frontend import frontend
    app.register_blueprint(admin)
    app.register_blueprint(frontend)

    return app