import dash
from flask import Flask
from flask.helpers import get_root_path

from config import BaseConfig


def create_app():
    server = Flask(__name__)
    server.config.from_object(BaseConfig)

    register_dashapps(server)
    register_blueprints(server)

    return server


def register_dashapps(app):
    from app.dash_app.layout import layout
    from app.dash_app.callbacks import register_callbacks

    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dashapp1 = dash.Dash(__name__,
                         server=app,
                         url_base_pathname='/dashboard/',
                         assets_folder=get_root_path(__name__) + '/dashboard/assets/',
                         meta_tags=[meta_viewport])

    with app.app_context():
        dashapp1.title = 'Dashapp 1'
        dashapp1.layout = layout
        register_callbacks(dashapp1)




def register_blueprints(server):
    from app.webapp import server_bp

    server.register_blueprint(server_bp)
