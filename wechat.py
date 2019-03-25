# -*- coding: UTF-8 -*-

import itchat
import json


import itchat 
import random


itchat.login()
itchat.auto_login(hotReload=True)

friends_list = itchat.get_friends(update=True)
print(type(friends_list))
for friend in friends_list:
    print(type(friend))
     
    #print(friends_list[:3])
#for i in friends_list[1:]:
#    print(i)
#name = itchat.search_friends(name=u'小纯洁')
#print(name)
#XiaoMing = name[0]

#message_list = [u'Hey,dude',u'Are you ok?',u'Bye~']
#message_concent = random.sample(message_list,1)[0]
#itchat.send('1111111',toUserName=XiaoMing)



# 登录

'''
# 发送消息
friends_list = itchat.get_friends(update=True)
itchat.send(u'你好', 'filehelper')
name=itchat.search_friends(name=u'Andy')
Andy = name[0]["UserName"]
print(Andy)
itchat.send("111111111", Andy)'''
'''
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]


# 初始化计数器，有男有女，当然，有些人是不填的
male = female = other = 0

# 遍历这个列表，列表里第一位是自己，所以从"自己"之后开始计算
# 1表示男性，2女性
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1

# 总数算上，好计算比例啊～
total = len(friends[1:])

# 好了，打印结果
print u"男性好友：%.2f%%" % (float(male) / total * 100)
print u"女性好友：%.2f%%" % (float(female) / total * 100)
print u"其他：%.2f%%" % (float(other) / total * 100)

'''
