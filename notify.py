#! /usr/bin/python3

# Copyright(c) 2020 note.jorhelp.cn

# Authored by Jorhelp on: 2020年 01月 21日 星期二 10:48:54 CST

# @desc: 通过notify-send来显示任务

import os, time, datetime
from configparser import ConfigParser


#====================================
# 读取配置文件
#====================================
config=ConfigParser()
user_path=os.path.expanduser("~")
config_path=user_path+"/.config/task/taskrc"
config.read(config_path, encoding='UTF-8')


#====================================
# 全局变量
#====================================
FILE_NAME=config['file']['name']
SWITCH=config['notify']['switch']
INTERVAL=config['notify']['interval']
OLDTIME=datetime.datetime.now()
NEWTIME=datetime.datetime.now()



#====================================
# notify-send
#====================================
def notifySend():
#用os.path.exit()也可以，但如果有一个同名的目录的话就不好办了
    if(os.path.isfile(FILE_NAME)):
        with open(FILE_NAME) as f:
            #文件上次修改时间
            file_time= time.localtime(os.stat(FILE_NAME).st_mtime)

            tasks=f.readlines()
            Ptasks=[]
            for i in tasks:
                if i.strip()!="" and not i.strip().startswith("//"):
                    Ptasks.append(i.strip())

            msg="\n"

            # 没有任务
            if len(Ptasks)==0:
                os.system("notify-send -t 30000 'Wow! You have finished all the tasks!'")

            else:
                num=1
                for i in Ptasks:
                    if i[0]=="+":
                        task=i[1:].strip()
                        msg+=str(num)+". "+task+'\n'
                        num+=1
                    else:
                        pass


                #文件上次修改时间
                msg += "\n> "+time.strftime("%Y-%m-%d %H:%M",file_time)
                os.system("notify-send -i none -t 30000  'Your tasks' '" + msg +"'")

#没有这个文件
    else:
        try:
            os.system("notify-send -u critical 'no task file @_@'")
        except:
            pass

#====================================

if __name__ == "__main__":
    if SWITCH=="on":
        cumd=os.path.expanduser(config['file']['path'])
        #切换到主目录
        os.chdir(cumd)
        while True:
            NEWTIME=datetime.datetime.now()
            if (NEWTIME-OLDTIME).seconds//60==int(INTERVAL):
                notifySend()
                OLDTIME=NEWTIME
            time.sleep(5)
    else:
        pass
