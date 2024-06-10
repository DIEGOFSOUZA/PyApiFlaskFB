from flask import Flask
from .extensions import db
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .api.cliente import cliente_bp
    app.register_blueprint(cliente_bp, url_prefix='/api/clientes')

    return app
