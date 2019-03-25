# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 21:31:49 2018

@author: 陈开锋
"""

import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    context_msg=msg.text
    #print(context_msg)
    if context_msg.isdigit():
        num=int(context_msg)
        ret_Message="连续次数设置为：%(cishu)d "%{'cishu':num}
        if msg['User']['RemarkName']==u"陈开锋":
            print("陈开锋")
        
    else:
        num=5
        ret_Message="请输入数字，连续次数默认为5"
    return ret_Message
        
    #msg.user.send('%s: %s' % (msg.type, msg.text))
'''
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)


@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    if msg.isAt:
        msg.user.send(u'@%s\u2005I received: %s' % (
            msg.actualNickName, msg.text))
'''
itchat.logout()
#itchat.auto_login(True)
#itchat.run()
