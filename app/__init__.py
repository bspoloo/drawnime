from flask import Flask
from .config import Config
from app.controllers.home_controller import home_bp
import os

def create_app():
    # Configurar las rutas de templates y static correctamente
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object(Config)
    
    
    app.register_blueprint(home_bp)
    
    return app