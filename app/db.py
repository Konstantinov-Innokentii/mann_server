from flask_sqlalchemy_session import flask_scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy_utils.listeners import force_auto_coercion

from app import app


def create_session_factory():
    engine = create_engine(app.config['DATABASE_URL'], echo=app.config['DATABASE_DEBUG_SQL'] and app.config['DATABASE_DEBUG_SQL'])

    Session = sessionmaker()
    Session.configure(bind=engine, autoflush=False, autocommit=False)

    return Session


session = flask_scoped_session(create_session_factory())


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


class Base(object):

    @property
    def bound_session(self):
        return object_session(self)


Base = declarative_base(cls=Base, metadata=MetaData(naming_convention=convention))

force_auto_coercion()