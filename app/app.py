"""A simple flask web app"""
from flask import Flask, render_template

from .controllers.page4_controller import Page4Controller
from .controllers.index_controller import IndexController
from werkzeug.debug import DebuggedApplication

from .controllers.page1_controller import Page1Controller
from .controllers.page2_controller import Page2Controller
from .controllers.page3_controller import Page3Controller


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
    return app

api = create_app()

@api.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@api.route("/page1", methods=['GET'])
def page1_get():
    return Page1Controller.get()

@api.route("/page2", methods=['GET'])
def page2_get():
    return Page2Controller.get()
@api.route("/page3", methods=['GET'])
def page3_get():
    return Page3Controller.get()

@api.route("/page4", methods=['GET'])
def page4_get():
    return Page4Controller.get()