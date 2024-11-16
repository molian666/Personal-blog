from flask import Blueprint
from flask import render_template
from .models import Post

"""创建一个博客的蓝图"""
bp_blog = Blueprint('blog', __name__, url_prefix='/blog', static_folder='static', template_folder='templates')


@bp_blog.route('/index')
def index():
    return render_template('index.html', **locals())


@bp_blog.route('/Email')
def email():
    return 'molian6666@gmail.com'
