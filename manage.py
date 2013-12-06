from flask.ext.script import Manager
from app import create_app, db
from app.auth.models import *
from app.forum.models import *

manager = Manager(create_app())

@manager.command
def create():
    """ cree les tables de la base de donnees
    """
    db.create_all()

@manager.command
def drop():
    """ drop database tables
    """

    db.drop_all()

if __name__ == '__main__':
    manager.run()