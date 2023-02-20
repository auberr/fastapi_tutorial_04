from sqlmodel import SQLModel, Session, create_engine
from models import Department, Employee

DB_FILE = 'db.sqlite3'
engine = create_engine(f"sqlite:///{DB_FILE}", echo=True, connect_args={"check_same_thread": False})

def create_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

if __name__ == '__main__':
    create_tables()
