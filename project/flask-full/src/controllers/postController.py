from flask import render_template, flash, redirect, url_for, abort, request
from flask_login import current_user
from src.forms.PostForm import PostForm
from src.forms.PostUpdateForm import PostUpdateForm
from src.models.post import Post
from src.models.user import User
from src.models import db

def index():
    #post = Post.query.all()
    page =  request.args.get('page', 1, type=int)
    post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)
    return render_template('post.html', post=post)


def create():
    form = PostForm()
    return render_template('post-create.html', form=form)

def store():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'successfully account create', 'success')
        return redirect(url_for('dashboard.index'))

    return render_template("post-create.html", form=form)


def show(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostUpdateForm()
    form.title.data = post.title
    form.content.data = post.content
    return render_template('post-show.html', post=post, form=form)


def update(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostUpdateForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash(f'successfully post update', 'success')
        return redirect(url_for('dashboard.index'))

def delete(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'successfully post delete', 'success')
    return redirect(url_for('dashboard.index'))


def user_posts(username):
    page = request.args.get('page',1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user).order_by(Post.date_posted.desc()).paginate(page=page, per_page=2)

    print(page)
    print(user)
    print(posts)

    return "112233"
