from bottle import run, route, view, static_file, template, request, response
from datetime import *

import sys
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import DateTime

"""
CLASSES
"""

# base class for all table-related classes
Base = declarative_base()

# Player CLASS goes here
class Player(Base):
    __tablename__ = 'Player'
    studentid = Column(Integer,primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    DOB = Column(String)
    experience = Column(Integer)

    def __repr__(self):
        return f"Player: id={self.studentid}, name={self.firstname} {self.lastname}, DOB={self.DOB}"

    def description(self):
         return f"Player: id={self.studentid}, name={self.firstname} {self.lastname}, DOB={self.DOB}"
""""""

#setup the static files routes first
#this allows bottle to use css files (files that do not change)
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')


@route('/')
#@view('index')
def index():

    logoninfo = ['Not logged','No username','No password']
    #return dict(loggedon=loggedon)
    logon_ok =  request.cookies.get('logonok', 'Not Logged on') 
    username = request.cookies.get('username', '') 
    pwd  =  request.cookies.get('password', '') 
    logoninfo = [logon_ok,username,pwd]
    return template('login', loggedon=logoninfo)
    pass

@route('/login', method='post')
#@view('index')
def login():
    username = request.forms.get('username','')
    pwd = request.forms.get('password','')
    logon_ok = request.cookies.get('logonok','New Logon')
    response.set_cookie('username', username)
    response.set_cookie('password', pwd)
    response.set_cookie('logonok', 'logon_ok')
    logoninfo = [logon_ok,username,pwd]
    #return dict(loggedon=loggedon)
    return template('login', loggedon=logoninfo)
    pass

@route('/list')
def list():
    #return "list page"


   
    # LIST ALL code goes here
    # get a list of the players by using session.query
    # players is a list. each item in the list is a player object.
    #players = session.query(Player).all()
    today = date.today()
    players = session.query(Player)
    return template('list.tpl', players=players,day=today)

@route('/edit')
def edit():
    #get the id from the query string
    id = request.query.id
    #get a student object
    #open a session
    db_engine = create_engine('sqlite:///db/Players.db')
    #dynamic class creation - creates a sessionmaker class
    Session = sessionmaker(bind=db_engine)
    #object creation
    session = Session()
    player = session.query(Player).filter_by(studentid=id).one()
    return template('edit.tpl',p = player)

# SQL CONNECTION goes here
db_engine = create_engine('sqlite:///db/Players.db')

# dynamic class creation - creates a sessionmaker class
Session = sessionmaker(bind=db_engine)
#object creation
session = Session()

    # Start the website
run(host='127.0.0.1', port=8080, reloader=True, debug=True) 