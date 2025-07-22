from db.models.chat_history import Base
from db.database import engine

Base.metadata.create_all(bind=engine)
