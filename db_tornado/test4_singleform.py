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

class User(Base):
    __tablename__ = 't_cuser'
    userid = Column(Integer, primary_key=True, autoincrement=True)
    uname = Column(String(length=20))
    birth = Column(Date)

class Address(Base):
    __tablename__ = 't_address'
    aid = Column(Integer, primary_key=True, autoincrement=True)
    aname = Column(Text)

# 4：使用session技术来创建连接池
from sqlalchemy.orm import sessionmaker
import datetime
def insertUser(uname):
    connpool = sessionmaker(bind=engine)
    # 获取一个连接
    conn = connpool()
    # 创建一个user对象
    user = User(uname=uname,birth=datetime.datetime.today())
    # 插入到t_cuser表中
    conn.add(user)
    conn.commit()
    conn.refresh(user)
    conn.close()
    return user

# insertUser('Theshy')

# 一次性插入多个数据
def insertMany(users=[]):
    # 创建连接池
    connpool = sessionmaker(bind=engine)
    # 获取连接
    conn = connpool()
    # 一次性插入多个数据
    conn.add_all(users)
    # 提交事物，刷新，再断开连接
    conn.commit()
    [conn.refresh(u) for u in users]
    conn.close()
    return users

# user1 = User(uname='lisi',birth=datetime.datetime.today())
# user2 = User(uname='wangwu',birth=datetime.datetime.today())
# userList = [user1,user2]
# insertMany(userList)

user3 = User(uname='zhangjie',birth=datetime.datetime.today())
addr = Address(aname='beijingshi')
uaList = [user3,addr]
insertMany(uaList)