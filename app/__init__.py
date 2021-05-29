from flask import Flask
from .config import Config
from .db import db

def create_app():
    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.config.from_object(Config)
    
    db.init_app(app)

    from .main import main_bp
    app.register_blueprint(main_bp)

    return app