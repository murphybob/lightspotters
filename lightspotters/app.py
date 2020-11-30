import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from sentry_sdk.integrations.flask import FlaskIntegration

from lightspotters.api import api
from lightspotters.main import main

import sentry_sdk

environment = os.environ.get('FLASK_ENV', 'production')

if environment != 'development':
    sentry_sdk.init(
        "https://4addc4e9e13840a1bd4bd82547ddcb67@o484528.ingest.sentry.io/5537806",
        traces_sample_rate=1.0,
        integrations=[FlaskIntegration()]
    )


def create_app():
    app = Flask(__name__)

    # CORS in dev only
    if environment == "development":
        CORS(app)

    # Setup the database
    from lightspotters.models import db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///../db.sqlite3')
    Migrate(app, db)
    db.init_app(app)
    db.app = app

    # Register routes
    app.register_blueprint(main)
    app.register_blueprint(api, url_prefix='/api')

    return app
