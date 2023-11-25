from flask import Flask
from importlib import import_module


def create_app():
    app = Flask(__name__, static_url_path='/static')

    for module in ['home', 'product']:
        module = import_module(f'app.{module}.routes')
        app.register_blueprint(module.blueprint)
        print(f'Loaded {module}')

    return app
