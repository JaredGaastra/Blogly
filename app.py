from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, connect_db, Users, Posts

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "secret"

app.app_context().push() 

connect_db(app)

@app.route('/')
def home():
    """list of users"""

    users = Users.query.all()
    return render_template('home.html', users=users)

@app.route('/new/users', methods=['GET', 'POST'])
def new_user():
    """new user form"""
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name  = request.form['last_name']
        image_url  = request.form['email'] or None

        new_user = Users(first_name=first_name, last_name=last_name, image_url=image_url)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('new_user.html')

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    """user detail"""
    
    user = Users.query.get_or_404(user_id)
    return render_template('user_detail.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    """edit user"""
    user = Users.query.get_or_404(user_id)
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name  = request.form['last_name']
        user.image_url  = request.form['email'] or None

        db.session.commit()

        return redirect(url_for('home'))
    return render_template('edit_user.html', user=user)

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """delete user"""
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/users/<int:user_id>/posts/new', methods=['GET', 'POST'])
def add_post(user_id):
    """adding a post for specific user"""
    user = Users.query.get_or_404(user_id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        new_post = Posts(title=title, content=content, user_id=user_id)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('user_detail', user_id=user_id))
    return render_template('user_post.html', user=user)