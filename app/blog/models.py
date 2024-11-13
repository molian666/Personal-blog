from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

tag_post_association = db.Table(
    'tag_post_association',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag_db.id')),
    db.Column('post_id', db.Integer, db.ForeignKey('post_db.id'))
)

tag_note_association = db.Table(
    'tag_note_association',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag_db.id')),
    db.Column('note_id', db.Integer, db.ForeignKey('note_db.id'))
)


class Base(db.Model):
    """基础类型"""
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键')
    create_time = db.Column(db.DateTime, nullable=False, default=datetime.now(), comment='创建时间')
    update_time = db.Column(db.DateTime, nullable=False, default=create_time, onupdate=datetime.now(),
                            comment='更新时间')


class Post(Base):
    """帖子模型"""
    __tablename__ = 'post_db'
    title = db.Column(db.String(128), nullable=False, comment='帖子标题')
    content = db.Column(db.Text, nullable=False, comment='帖子内容')
    draft = db.Column(db.Boolean, default=True, comment='草稿')
    cover = db.Column(db.String(32), nullable=False, comment='帖子封面路径')
    comments = db.relationship('Comment', backref='post')
    user_id = db.Column(db.Integer, db.ForeignKey('user_db.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('category_db.id'))
    attachments = db.relationship('Attachment', backref='post')
    tags = db.relationship('Tag', secondary=tag_post_association, backref='post')


class Comment(Base):
    """评论模型"""
    __tablename__ = 'comment_db'
    content = db.Column(db.Text, nullable=False, comment='评论内容')
    ip = db.Column(db.Integer, nullable=False, comment='ip')
    address = db.Column(db.String(64), nullable=False, comment='地址')
    post_id = db.Column(db.Integer, db.ForeignKey('post_db.id'))
    replied_id = db.Column(db.Integer, db.ForeignKey('comment_db.id'))
    replied = db.relationship('Comment', backref='replies', remote_side='Comment.id', cascade='delete')


class Message(Base):
    """留言模型"""
    __tablename__ = 'message_db'
    content = db.Column(db.Text, nullable=False, comment='留言内容')
    ip = db.Column(db.Integer, nullable=False, comment='ip')
    address = db.Column(db.String(64), nullable=False, comment='地址')


class User(Base):
    """用户模型"""
    __tablename__ = 'user_db'
    name = db.Column(db.String(64), nullable=False, comment='昵称')
    account = db.Column(db.String(64), nullable=False, unique=True, comment='账号')
    password = db.Column(db.String(64), nullable=False, comment='密码')
    brief = db.Column(db.String(64), nullable=False, comment='简介')
    posts = db.relationship('Post', backref='user')


class Tag(Base):
    """标签模型"""
    __tablename__ = 'tag_db'
    name = db.Column(db.String(64), nullable=False, comment='标签名')
    color = db.Column(db.String(64), nullable=False, comment='标签颜色')
    category_id = db.Column(db.Integer, db.ForeignKey('category_db.id'))


class Category(Base):
    """分类模型"""
    __tablename__ = 'category_db'
    name = db.Column(db.String(64), nullable=False, comment='分类名')
    posts = db.relationship('Post', backref='category')
    tags = db.relationship('Tag', backref='category')
    notes = db.relationship('Note', backref='category')


class Note(Base):
    """笔记模型"""
    __tablename__ = 'note_db'
    title = db.Column(db.String(64), nullable=False, comment='笔记名')
    content = db.Column(db.String(64), nullable=False, comment='笔记内容')
    category_id = db.Column(db.Integer, db.ForeignKey('category_db.id'))
    attachments = db.relationship('Attachment', backref='note')
    tags = db.relationship('Tag', secondary=tag_note_association, backref='note')


class Attachment(Base):
    """附件模型"""
    __tablename__ = 'attachment_db'
    name = db.Column(db.String(64), nullable=False, comment='附件名')
    path = db.Column(db.String(256), nullable=False, comment='附件路径')
    size = db.Column(db.Integer, nullable=False, comment='附件大小')
    note_id = db.Column(db.Integer, db.ForeignKey('note_db.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post_db.id'))
