#! /usr/bin/python3

# Copyright(c) 2020 note.jorhelp.cn

# Authored by Jorhelp on: 2020年 01月 20日 星期一 11:22:10 CST

# @desc: 安装脚本

import os

cumd=os.path.expanduser("~")
os.system("mkdir "+cumd+"/.config/test")
os.system("cp ./taskrc "+cumd+"/.config/test/taskrc")
os.system("sudo cp ./task.py /usr/local/bin/")

sh=os.system("echo 'task.py' >> "+cumd+"/.bashrc")
sh=os.system("echo 'task.py' >> "+cumd+"/.zshrc")

print(" Finished !!")
