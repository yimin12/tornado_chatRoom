import torndb

def insert(clsname, sname, coursenames=[]):
    # 1. 建立连接
    conn = torndb.Connection(host='127.0.0.1', database='tornado_test', user='root', password='123456')
    # 2. 先插入班级表数据
    clsList = conn.query('select cno from t_cls where cname="%s"'%clsname)
    print(clsList)
    if clsList:
        clsid = clsList[0]['cno']
    else :
        clsid = conn.insert('insert into t_cls values(null, "%s")'%clsname)

    # 3. 再插入学生表数据
    stuList = conn.query('select sno from t_student where sname="%s"'%sname)
    if stuList:
        sno = stuList[0]['sno']
    else :
        sno = conn.insert('insert into t_student values(null, "%s", "%s")'%(sname, clsid))

    # 4. 再插入课程表
    courseid_list = []
    for cn in coursenames:
        courseList = conn.query('select courseid from t_course where coursename="%s"'%cn)
        if courseList:
            courseid_list.append(courseList[0]['courseid'])
        else :
            cid = conn.insert('insert into t_course values(null, "%s")'%cn)
            courseid_list.append(cid)

    # 5. 插入中间表
    for courseid in courseid_list:
        conn.insert('insert into t_sc values(null, "%s", "%s")'%(sno, courseid))

    conn.close()
insert('Python', 'TheShy',['HTML5', 'CSS3'])