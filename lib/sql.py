#!/usr/bin/env python
#
# this is the sql class to operate database by leveraging sqlalchemy
#

import os, sys
from sqlalchemy import create_engine, text, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                'conf'))
from setting import *


Base = declarative_base()  
  
class Testtb1(Base):  
    __tablename__ = 'test_tb1'  
  
    id   = Column(Integer, Sequence('id'), primary_key=True)  
    name = Column(String)  
    type = Column(String)  
  
    def __repr__(self):  
        return "<Testtb1: (id='%d', name='%s', type='%s')>" % \
            (self.id, self.name, self.type)

class Mysql():
    def __init__(self):
        engine = create_engine(DB_CONN, echo=DB_ECHO)
        Session = sessionmaker(bind=engine)  
        self.session = Session()

    def query(self, table=None, key='', value=''):
        if table == None or key == '' or value == '':
            print("Please set correct parameters!!!")
            return None
        else:
            return self.session.query(table).filter(text("%s=%s" % \
                    (key, value))).one()

    def queryall(self, table=None):
        if table == None:
            print("Please set correct table!!!")
            return None
        else:
            return self.session.query(table).all()

    def update(self, table=None, key='', value='', mkey='', mvalue=''):
        if table == None or key == '' or value == '':
            print("Please set correct parameters!!!")
            return
        else:
            self.session.query(table).filter("%s=%s" % (key, value))\
                    .update({mkey:mvalue})
            self.session.commit()

    def __del__(self):
        self.session.close()

