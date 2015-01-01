#!/usr/bin/env python
# coding: utf-8

from __future__ import division, print_function, unicode_literals

import bcrypt
from sqlalchemy import (Boolean, Column, create_engine, Date, DateTime,
                        ForeignKey, func, Integer, Numeric, select, Sequence,
                        String, Table, Text, text, Unicode, UnicodeText)
from sqlalchemy.dialects.postgresql import ENUM, JSON
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.orm import (backref, column_property, object_session,
                            relationship, scoped_session, sessionmaker,
                            validates)

from settings import SQLALCHEMY_DATABASE_URI
JSON = MutableDict.as_mutable(JSON)

Base = declarative_base()

def get_session(engine=SQLALCHEMY_DATABASE_URI):
    Session = sessionmaker()
    engine = create_engine(engine, echo=False)
    Session.configure(bind=engine)
    session = Session()
    return session

class Post(Base):
    __tablename__ = 'topics'
    id = Column(Integer, primary_key = True )
    text = Column(UnicodeText)
    username = Column(Unicode)
    comment_id = Column(Unicode, unique = True)



