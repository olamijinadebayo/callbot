
from flask import Flask
from config import config_options





def create_app(config_state):
    app = Flask(__name__)
    app.config.from_object(config_options[config_state])


    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
