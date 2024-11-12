from flask import Flask
from app.blog.views import bp_blog  # 导入blog蓝图
from app.blog.models import db
from flask_migrate import Migrate


def create_app():
    """实例化app"""
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    """注册蓝图"""
    app.register_blueprint(bp_blog)
    """初始化数据库"""
    db.init_app(app)
    """初始化迁移对象"""
    migrate = Migrate(app, db)


    return app