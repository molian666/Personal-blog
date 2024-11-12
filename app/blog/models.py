from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键')
    title = db.Column(db.String(128), nullable=False, comment='标题')
    content = db.Column(db.Text, nullable=False, comment='内容')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, default=create_time, onupdate=datetime.now(), comment='更新时间')






