import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    
class Follower(Base):
    __tablename__ = 'Follower'
    user_from_id = Column(Integer, ForeignKey('User.id'), primary_key= True )
    user_to_id = Column(Integer, ForeignKey('User.id'))
       
    relacionfollower = relationship('User')

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    tipo = Column(enum)
    post_id = Column(Integer), ForeignKey('post')

    relacionmedia = relationship('Post')

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer), ForeignKey('User.id')

    relacionpost = relationship('User')

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(500))
    author_id = Column(Integer), ForeignKey('User.id')
    post_id = Column(Integer), ForeignKey('Post.id')

    relacioncomment = relationship('User')
    relacioncomment = relationship('Post')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e