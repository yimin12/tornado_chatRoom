from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

# 1: 创建engine对象 光使用mysql会报错
conn_url = 'mysql+pymysql://root:123456@127.0.0.1:3306/tornado_test?charset=UTF8MB4'
engine = create_engine(conn_url,encoding='utf-8',echo=True)
# 2：创建ORM对象
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

# 3: 引入列和字段信息
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, Date, DateTime, Float, Text

class Clazz(Base):
    __tablename__= 't_cls'
    cno = Column(Integer, primary_key=True,autoincrement=True)
    cname = Column(String(length=30),unique=True)
class Student(Base):
    __tablename__='t_student'
    sno = Column(Integer, primary_key=True, autoincrement=True)
    sname = Column(String(length=30),unique=True)
    cno = Column(Integer, ForeignKey(Clazz.cno,ondelete='CASCADE',onupdate='CASCADE'))
    def __repr__(self):
        return u'<Student:%s>'%self.sname

class Course(Base):
    __tablename__='t_course'
    courseid = Column(Integer,primary_key=True, autoincrement=True)
    coursename = Column(String(length=30),unique=True)

class SC(Base):
    __tablename__='t_sc'
    id = Column(Integer,primary_key=True,autoincrement=True)
    sno = Column(Integer, ForeignKey(Student.sno,onupdate='CASCADE',ondelete='CASCADE'))
    courseid = Column(Integer, ForeignKey(Course.courseid,onupdate='CASCADE',ondelete='CASCADE'))

# 对于有外键的元素，应该注意插入的顺序
def insertMany(cname,sname,coursenames=[]):
    from sqlalchemy.orm import sessionmaker
    connpool = sessionmaker(bind=engine)
    conn = connpool()
    # step 1: 插入学生表
    clsList = conn.query(Clazz.cno).filter(Clazz.cname==cname).all()
    if clsList:
        cno = clsList[0].cno
    else :
        cls = Clazz(cname=cname)
        conn.add(cls)
        conn.commit()
        conn.refresh(cls)
        cno = cls.cno
    # step 2: 插入学生数据表
    stuList = conn.query(Student.sno).filter(Student.sname==sname).all()
    if stuList:
        sno = stuList[0].sno
    else :
        stu = Student(sname=sname,cno=cno)
        conn.add(stu)
        conn.commit()
        conn.refresh(stu)
        sno = stu.sno

    # step 3: 插入课程表数据
    courseid_list = []
    for cn in coursenames:
        courseList = conn.query(Course.courseid).filter(Course.coursename==cn).all()
        if courseList:
            courseid_list.append(courseid_list[0].courseid)
        else:
            course = Course(coursename=cn)
            conn.add(course)
            conn.commit()
            conn.refresh(course)
            courseid_list.append(course.courseid)

    # step 4: 插入中间表数据
    for cid in courseid_list:
        sc = SC(sno=sno,courseid=cid)
        conn.add(sc)
        conn.commit()
        conn.refresh(sc)

    conn.close()
insertMany('Python207','Theshy',['Python','HTML5'])