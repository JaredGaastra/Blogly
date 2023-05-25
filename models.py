from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 


db = SQLAlchemy()

class PostTag(db.Model):
    """post tags"""

    __tablename__ = "post_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

class Tags(db.Model):
    """tags"""

    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    tag_posts = db.relationship('Posts', secondary='post_tags', back_populates='tags')



class Users(db.Model):
    """users"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name  = db.Column(db.String(50), nullable=False)
    image_url  = db.Column(db.String(500), nullable=True, default="https://www.freeiconspng.com/uploads/blue-user-icon-32.jpg")

    user_posts = db.relationship('Posts', back_populates='all_users', foreign_keys='Posts.user_id')

    def __repr__(self):
        """show info about user"""
        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"


class Posts(db.Model):
    """posts created by users"""

    __tablename__= "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    tags= db.relationship('Tags', back_populates='tag_posts', secondary='post_tags')
   
    all_users = db.relationship('Users', back_populates='user_posts')

    def __repr__(self):
        """show info about post"""
        p = self
        return f"<Post {p.id} {p.title} {p.created_at}>"
    



def connect_db(app):
    """Connect to database"""
    db.app = app
    db.init_app(app)
