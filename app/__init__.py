from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config='config'):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('index.html')


    from auth.views import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    return app