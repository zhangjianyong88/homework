import pymysql
import time
import hashlib






# 使用pymysql创建一个数据库bbs
conn = pymysql.Connect(host='192.168.12.129',user='root',password='123456',port=3306,charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = "create database bbs"
res = cursor.execute(sql)
# print(1)
conn = pymysql.Connect(host='192.168.12.129', user='root', password='123456',db= 'bbs', port=3306, charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#数据库bbs中创建用户表user
sql =  """ create table if not exists user(uid tinyint PRIMARY KEY auto_increment,username CHAR(4) UNIQUE,usertype enum('1','0') DEFAULT '0',password CHAR(49),regtime datetime,email CHAR (20))"""
# print(1)
cursor.execute(sql)
# print(2)
#创建用户


while 1:
    print("******请选择业务********")
    print("******1、*注册用户******")
    print("******2、用户登录*******")
    print("******3、内容展示*******")
    sum = input("请输入：")
    if sum == 1:
       while True:
           sname = input('请输入账号')
           psql = "select username from user where username= %s"%sname
           # print(psql)
           if cursor.execute(psql):
               print('用户名已存在')
               break
           elif len(sname)<2 or sname == '  ':
               print('输入有误，请重新输入')
               break

           spasswd = input('请输入密码')
           smail = input('请输入邮箱')
           break
       spasswd = str(hashlib.sha1(spasswd.encode('utf8')).hexdigest())
       stime = time.strftime('%Y-%m-%d',time.localtime(time.time()))
       # print(stime)
       sql_3 ="""insert into user (username,password,email,regtime) values (%s,'%s',%s,%s) """%(sname,spasswd,smail,stime)

       try:
           res = cursor.execute(sql_3)
           if res:
               conn.commit()
               print('用户创建成功')
           else:
               conn.rollback()
               print('用户创建失败')
       except Exception as e:
               print(e)
               conn.rollback()
       cursor.close()
       conn.close()
    if sum == 2:
        username = input("请输入用户名")
        password = input("请输入密码")
        password = hashlib.sha1(password.encode('utf8')).hexdigest()
        # 验证
        sql = "select username,password from user where username=%s and password=%s"
        res = cursor.execute(sql, [username, password])
        # print(res)
        if res > 0:
            print("登录成功")
        else:
            print("登录失败")
        cursor.close()
        conn.close()
    if sum == 3:
        sql_1 = 'select uid,username,password,usertype,regtime,email from user'
        cursor.execute(sql_1)
        print(cursor.fetchall())
        # 关闭
        cursor.close()
        conn.close()





















