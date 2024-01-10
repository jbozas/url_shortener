from sqlmodel import Session, SQLModel, create_engine

from settings import settings


engine = create_engine(
    settings.DATABASE_URI, echo=True, connect_args={"check_same_thread": False}
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
