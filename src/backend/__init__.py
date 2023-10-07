from flask import Flask


def create_app():
    print("hi")
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    return app
