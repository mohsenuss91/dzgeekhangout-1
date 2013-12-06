from app import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=False)
    password = db.Column(db.String(84), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)


    def set_password(self):
        pass

    def check_password(self):
        pass