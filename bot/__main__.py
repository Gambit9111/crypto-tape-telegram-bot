from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from .websocketer import WebSocketer
from .config import POSTGRES_URL
from .models import Base

# create db engine
engine = create_engine(POSTGRES_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# check if table exists
exist = inspect(engine).has_table("trades")
if not exist:
   print("Running for the first time. Creating table - users")
   Base.metadata.create_all(engine)
else:
   print("Table trades - already exists")

socket = WebSocketer(session)
socket.streamTrade()