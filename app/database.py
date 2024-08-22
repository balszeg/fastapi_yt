from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def _declarative_constructor(self, **kwargs):
    """Don't raise a TypeError for unknown attribute names."""
    cls_ = type(self)
    for k in kwargs:
        if not hasattr(cls_, k):
            continue
        setattr(self, k, kwargs[k])

Base = declarative_base(constructor=_declarative_constructor)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# This commented part shows how to connect to postgres database with raw SQL method
'''error_counter = 0

while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="postgres", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful!")
        break

    except Exception as ex:
        print("Connection to database failed")
        print(f"Error: {ex}")
        time.sleep(3)
        error_counter += 1

    if error_counter >= 10:
        exit(-1)'''