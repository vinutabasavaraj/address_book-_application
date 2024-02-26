from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from pathlib import Path
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker



Base = declarative_base()

def get_db():
    '''
    Generator function to create and manage a database session for SQLite database operations.

    '''

    global engine, Session
    
    current_directory_path = Path(__file__).parents[2]
    properties_filename = current_directory_path/'properties.json'
    
    with open(properties_filename) as fp:
        properties = json.load(fp)

    properties
    
    path_to_db = properties["metadata_config"]["databaseName"]
    
    SQLALCHEMY_DATABASE_URL = "sqlite:///" +  path_to_db
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    session_factory = sessionmaker(bind=engine)

    Session = scoped_session(session_factory)

    db = Session()
    try:
        yield db
    finally:
        db.close()
        engine.dispose()

    Session.remove()

    