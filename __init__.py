# -*- coding:utf-8 -*-

import  database
from database.config_setting import db, date_time
from database.user_db import User
from database.role_db import Role
from database.user_group_db import Usergroup
from business.user_business import UserBusiness

# from business.role_business import RoleBusiness,Role


new_user = User(name='BiBy', sex='女', pwd='gel123', phone='135878783',
                organization=u'如家酒店', email='131220024@qq.com',
                create_by='SuperUser')

# 添加新用户到session:
db.session.add(new_user)
# 进行数据库交互, 但是事务并没有提交. 
db.session.flush()

# 添加新角色到 session:
new_role = Role(name='SKT', role_type='3', create_by='Super User')
db.session.add(new_role)
# db.session.flush()

nenber = db.session.query(User).filter(User.name == 'Rose').one()

nenber.roles.append(new_role)
roles = nenber.roles
print("用户-多角色显示：")
for role in roles:
    if role is not None:
        print(role)
# x = User.query.with_parent(r_user_role) 
# print x

group = Usergroup(name=u'弱鸡', create_by='Super User')
db.session.add(group)
print(group)
# nenber.group.append(group)

xxx = UserBusiness()
print(xxx)
# 查询所有用户列表
users = xxx.find_all_users()
if users is not None:
    for user in users:
        print(user)

# 通过用户id 来进行删除 (√)
# user = xxx.delete_user_by_id(18)
# print user

# 密码的更新，总提示参数不对。
# xxx.update_pwd(name='Brand',pwd=m.update('123'))

# 输出根据id 去查询用户信息
print('start\n')
user5 = xxx.find_user_by_id(1)
print('user - id ==5:', user5)

users = xxx.search_user_by_info('Brank', '1762388223')
for user in users:
    print(user)
# 提交即保存到数据库:
db.session.commit()

# 测试用法 
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
# role = db.session.query(Role).filter(Role.id=='5').one()
# 打印类型和对象的name属性:
# print 'type:', type(role)
# print 'role——name:', role.name
# print role

# users = db.session.query(User).all()
# user = db.session.query(User).filter(User.id=='2').one()
# print user

# 关闭session:
db.session.close()
