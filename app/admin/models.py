from start import db
from datetime import datetime


class Base(db.Model):
    """基础类型"""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, default=create_time, onupdate=datetime.now(),
                            comment='更新时间')


class User(Base):
    """用户模型"""
    __tablename__ = 'user_ad'
    name = db.Column(db.String(64), nullable=False, comment='昵称')
    account = db.Column(db.String(64), nullable=False, unique=True, comment='账号')
    password = db.Column(db.String(64), nullable=False, comment='密码')
    last_login = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), comment='最后登录时间')
    avatar_path = db.Column(db.String(256), comment='头像路径')


class BlogInfo(Base):
    __tablename__ = 'bloginfo_ad'
    title = db.Column(db.String(64), nullable=False, comment='网站标题')
    subtitle = db.Column(db.String(64), comment='网站副标题')
    about_me = db.Column(db.Text, comment='关于我')
