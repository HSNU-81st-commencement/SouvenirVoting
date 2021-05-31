from logging.handlers import RotatingFileHandler
from datetime import datetime
from flask import Flask, current_app
from .config import Config
from .db import db


def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(Config)

    db.init_app(app)

    log_handler = RotatingFileHandler(
        "flask.log", mode="a", maxBytes=5 * 1024 * 1024, backupCount=2
    )
    log_handler.setLevel("INFO")
    app.logger.addHandler(log_handler)

    from .main import main_bp

    app.register_blueprint(main_bp)

    return app


def log(request):
    current_app.logger.info(
        " ".join(
            [
                datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                request.remote_addr,
                request.method,
                request.path,
            ]
        )
    )
