from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column, String,DateTime,Integer,create_engine
import os
conn = "sqlite:///D:/GITHUB/MERE_WALE/Resurgence/Database/Databases/TournamentDB.db"
db = create_engine(conn,echo = True)
Session = sessionmaker()
local = Session(bind=db)