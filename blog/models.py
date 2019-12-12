from . import db,login_manager

class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    full_name=db.Column(db.String(40),nullable=False)
    username=db.Column(db.String(20),nullable=False,unique=True)
    email=db.Column(db.String(80),nullable=False,unique=True)
    password=db.Column(db.String(40),nullable=False)

    def __repr__(self):
        return "{}".format(self.username)

        
    