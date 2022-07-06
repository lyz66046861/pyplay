import os
import sys

#open path ./logs mkdir bkp move file into dir ./logs/bkp
#打开路径./logs，创建目录bkp，将文件移动到目录./logs/bkp
#mkdir logs_backup if not exists
if not os.path.exists("logs_backup"):
   os.makedirs("logs_backup")
os.makedirs("logs_backup/%s"%sys.argv[1])
os.system("move /y %s logs_backup/%s"%(sys.argv[1],sys.argv[1]))
#mkdir name args[1] in logs_backup
#创建目录args[1]，在logs_backup目录下
# os.system("mkdir logs_backup/%s" % sys.argv[1])
# arg = input("Enter a file name:")
# print(arg)
# os.system("mkdir logs_backup/%s" %arg)
#move files in logs into dir ./logs/args[1]
#将logs目录下的文件移动到目录./logs/args[1]下
os.system("mv logs/* logs_backup/%s" % sys.argv[1])
# os.system("mv ./logs/* ./logs_backup/%s" % arg)
#将logs目录下的文件移动到目录./logs/args[1]
