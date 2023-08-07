from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///./sql_app.db", echo=True, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(engine)
