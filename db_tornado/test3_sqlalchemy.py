#coding=utf-8

from sqlalchemy.engine import create_engine

# 1: 创建engine对象 光使用mysql会报错
conn_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/tornado_test?charset=utf8'
engine = create_engine(conn_url,encoding='utf-8',echo=True)
# 2：创建ORM对象
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

# 3: 引入列和字段信息
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date, DateTime, Float, Text

# 4: 自定义类
class User(Base):
    __tablename__ = 't_cuser'
    userid = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(length=20))
    birth = Column(Date)

class Address(Base):
    __tablename__ = 't_address'
    aid = Column(Integer, primary_key=True, autoincrement=True)
    aname = Column(Text)
Base.metadata.create_all()
