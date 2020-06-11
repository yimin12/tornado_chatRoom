import torndb

'''
如果你是python3.x，记得修改torndb的源代码，可以按照如下教程
https://www.cnblogs.com/venz-seventeen/p/7818806.html
torndb默认使用的MySQLdb的模块，但是python3已经不使用这个模块了
'''
# 创建数据库建立连接
# conn = torndb.Connection(host='127.0.0.1',database='tornado_test', user='root', password='123456')

def insertUser(uname, pwd):
    # 创建数据库连接
    conn = torndb.Connection(host='127.0.0.1', database='tornado_test', user='root', password='123456')
    # 执行插入操作
    rowid = conn.insert('insert into t_auser values(null, "%s", "%s", now())'%(uname,pwd))
    print(rowid)
    # 断开连接
    conn.close()
# insertUser('Rookie','123123')
def insertMany(args=[]):
    # 创建数据库连接
    conn = torndb.Connection(host='127.0.0.1', database='tornado_test', user='root', password='123456')
    sql = 'insert into t_auser values(null, %s, %s, now())'
    # 执行插入操作
    rowid = conn.insertmany(sql, args)
    print(rowid)
    conn.close()
# insertMany([('XiaoHu','123456'),('Uzi','123321')])

def queryAll():
    # 创建数据库连接
    conn = torndb.Connection(host='127.0.0.1', database='tornado_test', user='root', password='123456')
    sql = 'select * from t_auser'
    # 执行插入操作
    rowList = conn.query(sql)
    print(rowList)
    conn.close()
# queryAll()
def queryUser(uname,pwd):
    # 创建数据库连接
    conn = torndb.Connection(host='127.0.0.1', database='tornado_test', user='root', password='123456')
    sql = 'select * from t_auser where uname="%s" and pwd="%s"'%(uname,pwd)
    # 执行插入操作
    rowList = conn.query(sql)
    print(rowList)
    conn.close()
# queryUser('Uzi','123321')
'''模糊查询'''
def likeQuery(key):
    # 创建数据库连接
    conn = torndb.Connection(host='127.0.0.1', database='tornado_test', user='root', password='123456')
    sql = 'select * from t_auser where uname like "%%{uname}%%"'.format(uname=key)
    # 执行插入操作
    print(sql)
    rowList = conn.query(sql)
    print(rowList)
    conn.close()
# likeQuery('U')
def order_by_userid(param):
    # 创建数据库连接
    conn = torndb.Connection(host='127.0.0.1', database='tornado_test', user='root', password='123456')
    # 确定排序方式
    rule = 'ASC'
    columnname = param
    if param.startswith('-'):
        rule = 'DESC'
        columnname = param[1:]
    sql = 'select * from t_auser order by %s %s' % (columnname, rule)
    print(sql)
    # 执行插入操作
    rowList = conn.query(sql)
    print(rowList)
    conn.close()
# order_by_userid('-userid')
# order_by_userid('userid')

# 使用分页
def page_user(num, size=2):
    # 创建数据库连接
    conn = torndb.Connection(host='127.0.0.1', database='tornado_test', user='root', password='123456')
    sql = 'select * from t_auser limit %s,%s'%(((num-1)*size),size)
    rowList = conn.query(sql)
    print(rowList)
    conn.close()
# page_user(2)

# 更新语句
def update(uname, newpwd):
    # 创建数据库连接
    conn = torndb.Connection(host='127.0.0.1', database='tornado_test', user='root', password='123456')
    sql = 'update t_auser set pwd = "%s" where uname = "%s"'%(newpwd,uname)
    conn.update(sql)
    conn.close()
# update('Theshy','123123')

# 删除语句
def delete(uname):
    conn = torndb.Connection(host='127.0.0.1', database='tornado_test', user='root', password='123456')
    sql = 'delete from t_auser where uname="%s"'%(uname)
    conn.execute(sql)
    conn.close()
delete('TheShy')