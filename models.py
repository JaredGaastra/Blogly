from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy()


class Users(db.Model):
    """users"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name  = db.Column(db.String(50), nullable=False)
    image_url  = db.Column(db.String(500), nullable=True, default="https://www.freeiconspng.com/uploads/blue-user-icon-32.jpg")

    def __repr__(self):
        """show info about user"""
        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"
class Posts(db.Model):
    """posts created by users"""

    __tablename__= "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    users = db.relationship('Users', backref='posts')

    def __repr__(self):
        """show info about post"""
        p = self
        return f"<Post {p.id} {p.title} {p.created_at}>"
    

def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)
