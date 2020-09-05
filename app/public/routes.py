from flask import abort, render_template, current_app
from werkzeug.exceptions import NotFound
import logging

from app.models import Post
from . import public_bp

logger = logging.getLogger(__name__)
@public_bp.route("/")
def index():
    current_app.logger.info('Mostrando los posts del blog')
    logger.info('Mostrando los posts del blog')
    posts = Post.get_all()
    return render_template("public/index.html", posts=posts)


@public_bp.route("/p/<string:slug>/")
def show_post(slug):
    post = Post.get_by_slug(slug)
    if post is None:
        raise NotFound(slug)
    return render_template("public/post_view.html", post=post)
