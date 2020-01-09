#! /usr/bin/python3

# Copyright(c) 2019 note.jorhelp.cn

# Authored by Jorhelp on: 2019年 12月 23日 星期三 08:18:20 CST

# @desc: 一个任务展示程序

import os, time

#===========================================================
# 全局变量---目录相关
#===========================================================
#文件名，在用户主目录下
file_name=".my_task"
#获取当前用户主目录，不能直接用'～'
cumd=os.path.expanduser('~')
#切换到主目录
os.chdir(cumd)
#使用说明，创建文件是会写入文件
Instructions="//注释以双斜杠开头\n\n"+\
             "//每个任务以加号开头\n\n"+\
             "//若任务下有子任务，子任务以减号开头\n\n"+\
             "//可以随意缩进，也可以有任意空行"
#===========================================================



#===========================================================
# 全局变量---显示相关
#===========================================================
Tab="   "  #缩进
#Head 与 Tail 一头一尾是必须的
Head="\033["
Tail="\033[0m"
#粗体，下划线，闪烁必须放在颜色的前面
Bold="1;"  #粗体
Underline="4;"  #下划线
Flash="5;"  #闪烁
Red="31m"
Green="32m"
Yellow="33m"
Blue="34m"
Pink="35m"
Cyan="36m" #青色
White="37m"
#===========================================================




#===========================================================
# 打印任务
#===========================================================
os.system("clear")
print("\n"+Head+Bold+Yellow+Tab+"===============Your Task List==============="+Tail)



#用os.path.exit()也可以，但如果有一个同名的目录的话就不好办了
if(os.path.isfile(file_name)):
    with open(file_name) as f:
        #文件上次修改时间
        file_time= time.localtime(os.stat(file_name).st_mtime)

        tasks=f.readlines()
        Ptasks=[]
        for i in tasks:
            if i.strip()!="" and not i.strip().startswith("//"):
                Ptasks.append(i.strip())

        if len(Ptasks)==0:
            print(Tab+"Wow! You have finished all the jobs @_@\n")
        else:
            for i in Ptasks:
                if i[0]=="+":
                    task=i[1:].strip()
                    print("\n"+Head+Bold+Pink+Tab+"> "+task+Tail)
                elif i[0]=="-":
                    task=i[1:].strip()
                    print(Head+Bold+Cyan+Tab+Tab+"- "+task+Tail)
                else:
                    print("\n"+Head+Bold+Flash+Red+Tab+"@_@ 有一条非法格式!请检查"+Tail)


            #打印文件上次修改时间
            print("\n"+Head+Blue+Tab+"last modification time:  "+Tail, end="")
            print(Head+Bold+Flash+Green+time.strftime("%Y-%m-%d %H:%M",file_time)+Tail)

#没有这个文件，会尝试创建
else:
    print(Tab+"The file doesn't exits...\n")
    try:
        os.system("touch "+file_name)
        with open(file_name, 'w') as f:
            f.write(Instructions)
        print(Tab+"Well, I' have touched it~~\n")
    except:
        print(Tab+"Touch file falled, please check!!\n")

print(Head+Bold+Yellow+Tab+"--------------------------------------------\n"+Tail)
#===========================================================
