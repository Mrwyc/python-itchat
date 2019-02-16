# -*- coding: utf-8 -*-
__author__ = 'YongCong Wu'
# @Time    : 2019/2/15 10:45
# @Email   :  : 1922878025@qq.com
import itchat
import time


def weichart_login():
    itchat.auto_login(hotReload=True)
    rooms = itchat.get_chatrooms(update=True)
    return rooms


def send_info(info, userlist=[]):
    weichart_login()
    for str_user in userlist:
        room = itchat.search_friends(name=str_user)
        print(room)
        userName = room[0]['UserName']
        SendInfo = info
        try:
            itchat.send(SendInfo, toUserName=userName)
            print("success")
        except:
            print("fail")


def mass_send_info(sendInfo):
    mass_user = weichart_login()
    Info = sendInfo
    for friend in mass_user:
        itchat.send(Info % (friend['DisplayName'] or friend['NickName']), friend['UserName'])
        time.sleep(1)


select_input = input("选择:  1:群发, 2: 指定用户发送 ： ")
if int(select_input) == 2:
    Info = input('请输入发送消息: ')
    inputInfo = input('请输入用户名称: (以空格分开)')
    split_str = inputInfo.split()
    send_info(Info, split_str)
elif int(select_input) == 1:
    inputInfo = input('请输入发送的消息: ')
    mass_send_info(inputInfo)
else:
    print("请选择正确数值!")
