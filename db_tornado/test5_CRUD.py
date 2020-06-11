from sqlalchemy.engine import create_engine

# 1: 创建engine对象 光使用mysql会报错
conn_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/tornado_test?charset=UTF8MB4'
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

    def __repr__(self):
        return u'<User:%s,%s>'%(self.userid,self.uname)

class Address(Base):
    __tablename__ = 't_address'
    aid = Column(Integer, primary_key=True, autoincrement=True)
    aname = Column(Text)

from sqlalchemy.orm import sessionmaker
def queryAll(clsname):
    connpool = sessionmaker(bind=engine)
    conn = connpool()
    # 执行查询操作
    users = conn.query(clsname).all()
    conn.close()
    return users
# print(queryAll(User))

def order_by_user(clsname):
    connpool = sessionmaker(bind=engine)
    conn = connpool()
    # 执行查询操作
    # users = conn.query(clsname).order_by(clsname.userid.desc()).all()
    users = conn.query(clsname).order_by(clsname.userid.asc()).all()
    conn.close()
    return users
# print(order_by_user(User))
# 统计人数
def get_user_count(clsname):
    connpool = sessionmaker(bind=engine)
    conn = connpool()
    user_count = conn.query(clsname).count()
    conn.close()
    return user_count
print(get_user_count(User))

# 分页
def page_user(clsname, num, size=2):
    connpool = sessionmaker(bind=engine)
    conn = connpool()
    users = conn.query(clsname).offset((num-1)*size).limit(size).all()
    conn.close()
    return users
# print(page_user(User,2))

def get_user_userid(clsname, pk):
    connpool = sessionmaker(bind=engine)
    conn = connpool()
    user = conn.query(clsname).get(pk)

    conn.close()
    return user
# print(get_user_userid(User,3))

# 将共同点提取成装饰器
def conn_wrapper(func):
    def __wrapper(*args, **kwargs):
        from sqlalchemy.orm import sessionmaker
        connpool = sessionmaker(bind=engine)
        conn = connpool()
        response = func(conn, *args, **kwargs) # 只在这一步进行了执行操作
        conn.close()
        return response
    return __wrapper

# 执行删除操作
@conn_wrapper
def deleteUserByUserid(conn, clsname, userid):
    conn.query(clsname).filter(clsname.userid==userid).delete()
    conn.commit()
# deleteUserByUserid(clsname=User, userid=1)

# 执行更新操作
@conn_wrapper
def updateUser(conn, userObj):
    conn.add(userObj)
    conn.commit()
user = get_user_userid(User,'2')
user.uname = 'xiena'
# updateUser(user)

@conn_wrapper
def get_User_param(conn,clsname, uname):
    users = conn.query(clsname).filter(clsname.uname==uname).all()
    return users
# print(get_User_param(User, 'xiena'))

@conn_wrapper
def get_And_Or_Not(conn,clsname,uname1):
    from sqlalchemy import and_,or_,not_
    users = conn.query(clsname).filter(not_(or_(clsname.uname==uname1,clsname.userid==3))).all()
    return users
# print(get_And_Or_Not(User,'xiena'))

# 分组查询
@conn_wrapper
def group_by_user(conn,clsname):
    from sqlalchemy.sql.functions import func
    users = conn.query(func.count(clsname.userid),clsname.uname).group_by(clsname.uname).all()
    return users
# print(group_by_user(User))

@conn_wrapper
def part_user(conn,clsname):
    users = conn.query(clsname.userid, clsname.uname).all()
    return users
print(part_user(User))