from flask import Blueprint
from flask import render_template
from .models import Post

"""创建一个博客的蓝图"""
bp_blog = Blueprint('blog', __name__, url_prefix='/blog', static_folder='static', template_folder='templates')


@bp_blog.route('/index')
def index():
    post = Post.query.get(1)
    title = post.title
    content = post.content
    return render_template('index.html', **locals())










