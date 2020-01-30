from model import *
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBsession = sessionmaker(bind=engine)
session = DBsession()

def add_user(name,password):
	user_object = User(name=name,
		password=password)
	session.add(user_object)
	session.commit()

def query_user(name):
	return session.query(User).filter_by(name=name).first()

