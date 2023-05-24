from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, connect_db, Users, Posts
from datetime import datetime

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
    posts = Users.query.get_or_404(user_id).user_posts
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        new_post = Posts(title=title, content=content, user_id=user_id, created_at=datetime.now() )
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('user_detail', user_id=user_id, posts=posts))
    return render_template('user_post.html', user=user , posts=posts)

@app.route('/posts/<int:post_id>')
def post_detail(post_id):
    """post detail"""
    post = Posts.query.get_or_404(post_id)
    return render_template('post_detail.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
def edit_post(post_id):
    """edit post"""
    post = Posts.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content  = request.form['content']

        db.session.commit()

        return redirect(url_for('post_detail', post_id=post_id))
    return render_template('edit_post.html', post=post)

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    """delete post"""
    post = Posts.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return redirect(url_for('user_detail', user_id=post.user_id))



# TAG ROUTES--------------------------------------------------------------

@app.route('/tags', methods=['GET', 'POST'])
def tags():
    """list of tags"""
    tags = Tags.query.all()
    return render_template('tags.html', tags=tags)

@app.route('/tags/new', methods=['GET', 'POST'])
def new_tag():
    """new tag form"""
    if request.method == 'POST':
        name = request.form['name']

        new_tag = Tags(name=name)
        db.session.add(new_tag)
        db.session.commit()

        return redirect(url_for('tags'))
    return render_template('new_tag.html')

@app.route('/tags/<int:tag_id>')
def tag_detail(tag_id):
    """tag detail"""
    tag = Tags.query.get_or_404(tag_id)
    return render_template('tag_detail.html', tag=tag)

@app.route('/tags/<int:tag_id>/edit', methods=['GET', 'POST'])
def edit_tag(tag_id):
    """edit tag"""
    tag = Tags.query.get_or_404(tag_id)
    if request.method == 'POST':
        tag.name = request.form['name']

        db.session.commit()

        return redirect(url_for('tag_detail', tag_id=tag_id))
    return render_template('edit_tag.html', tag=tag)

@app.route('/tags/<int:tag_id>/delete', methods=['POST'])
def delete_tag(tag_id):
    """delete tag"""
    tag = Tags.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()

    return redirect(url_for('tags'))