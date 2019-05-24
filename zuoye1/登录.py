import pymysql
import hashlib
#连接数据库
conn = pymysql.Connect(host='192.168.12.129', user='root', password='123456',db= 'bbs', port=3306, charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#输入命令
# username = input("请输入用户名")
# password = input("请输入密码")
# password = hashlib.sha1(password.encode('utf8')).hexdigest()
# #验证
# sql = "select username,password from user where username=%s and password=%s"
# res = cursor.execute(sql,[username,password])
# # print(res)
# if res > 0:
#     print("登录成功")
# else:
#     print("登录失败")

#z展示

sql_1 = 'select uid,username,password,usertype,regtime,email from user'
cursor.execute(sql_1)
print(cursor.fetchall())
#关闭
cursor.close()
conn.close()
