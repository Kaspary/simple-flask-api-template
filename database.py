import sqlite3
from sqlalchemy import create_engine, event
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
from flask import current_app
from flask.cli import AppGroup


engine = create_engine(current_app.config['SQLALCHEMY_DATABASE_URI'])
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

BaseModel = declarative_base()
BaseModel.query = db_session.query_property()

database_cli = AppGroup('db')
current_app.cli.add_command(database_cli)

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, sqlite3.Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA journal_mode=wal")
        cursor.close()


@current_app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import user.models
    BaseModel.metadata.create_all(bind=engine)



@database_cli.command('init')
def init_db_command():
    """Init db"""
    init_db()
