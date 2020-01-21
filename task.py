#! /usr/bin/python3

# Copyright(c) 2019 note.jorhelp.cn

# Authored by Jorhelp on: 2019年 12月 23日 星期一 08:18:20 CST

# @version: 3.0

# @desc: 一个任务展示程序

import os, time
from configparser import ConfigParser


#====================================
# 读取配置文件
#====================================
config=ConfigParser()
user_path=os.path.expanduser("~")
config_path=user_path+"/.config/task/taskrc"
config.read(config_path, encoding='UTF-8')


#====================================
# 全局变量---目录相关
#====================================
FILE_NAME=config['file']['name']

cumd=os.path.expanduser(config['file']['path'])
#切换到主目录
os.chdir(cumd)
#使用说明，创建任务文件时会写入文件
INSTRUCTIONS="//注释以双斜杠开头\n\n"+\
             "//每个任务以加号开头\n\n"+\
             "//若任务下有子任务，子任务以减号开头\n\n"+\
             "//可以随意缩进，也可以有任意空行"


#====================================
# 全局变量---显示相关
#====================================
TAB="   "  #缩进
#HEAD 与 TAIL 一头一尾是必须的
HEAD="\033["
TAIL="\033[0m"
#粗体，下划线，闪烁必须放在颜色的前面
BOLD="1;"  #粗体
UNDERLINE="4;"  #下划线
FLASH="5;"  #闪烁
COLORS={
    "RED" : "31m",
    "GREEN" : "32m",
    "YELLOW" : "33m",
    "BLUE" : "34m",
    "PINK" : "35m",
    "CYAN" : "36m",
    "WHITE" : "37m",
}

FIRST_LEVEL_COLOR=COLORS[config['color']['first']]
SECOND_LEVEL_COLOR=COLORS[config['color']['second']]
BORDER_COLOR=COLORS[config['color']['border']]
DATE_COLOR=COLORS[config['color']['date']]





#====================================
# 打印任务
#====================================
os.system("clear")
print("\n"+HEAD+BOLD+BORDER_COLOR+TAB+"===============Your Task List==============="+TAIL)



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

        if len(Ptasks)==0:
            print(TAB+"Wow! You have finished all the jobs @_@\n")
        else:
            for i in Ptasks:
                if i[0]=="+":
                    task=i[1:].strip()
                    print("\n"+HEAD+BOLD+FIRST_LEVEL_COLOR+TAB+"> "+task+TAIL)
                elif i[0]=="-":
                    task=i[1:].strip()
                    print(HEAD+BOLD+SECOND_LEVEL_COLOR+TAB+TAB+"- "+task+TAIL)
                else:
                    print("\n"+HEAD+BOLD+FLASH+COLORS['RED']+TAB+"@_@ 有一条非法格式!请检查"+TAIL)


            #打印文件上次修改时间
            print("\n"+HEAD+DATE_COLOR+TAB+"last modification time:  "+TAIL, end="")
            print(HEAD+BOLD+FLASH+COLORS['GREEN']+time.strftime("%Y-%m-%d %H:%M",file_time)+TAIL)

#没有这个文件，会尝试创建
else:
    print(TAB+"The file doesn't exits...\n")
    try:
        os.system("touch "+FILE_NAME)
        with open(FILE_NAME, 'w') as f:
            f.write(INSTRUCTIONS)
        print(TAB+"Well, I' have touched it~~\n")
    except:
        print(TAB+"Touch file falled, please check!!\n")

print(HEAD+BOLD+BORDER_COLOR+TAB+"--------------------------------------------\n"+TAIL)
#====================================
