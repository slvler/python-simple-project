from flask import Blueprint
from src.controllers.postController import index, create, store, show, update, delete, user_posts

PostBp = Blueprint('post', __name__)

PostBp.route('/', methods=["GET"])(index)
PostBp.route('/create', methods=["GET"])(create)
PostBp.route('/store', methods=["POST"])(store)
PostBp.route('/show/<int:post_id>', methods=["GET"])(show)
PostBp.route('/edit/<int:post_id>/update', methods=["POST"])(update)
PostBp.route('/delete/<int:post_id>', methods=["GET"])(delete)
PostBp.route('/user/<string:username>', methods=["GET"])(user_posts)