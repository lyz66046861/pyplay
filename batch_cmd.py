import sys
import os

#create batch file if not exists
#创建批处理文件，如果不存在
if not os.path.exists("./logs/@batch@.txt"):
    with open("./logs/@batch@.txt", "w") as f:
        f.write("")
        f.close()
    #open and append @batch@.txt
    #打开@batch@.txt文件，将sys.argv[1:]写入文件
    #sys.argv[1:]是命令行参数
with open('./logs/@batch@.txt', 'w') as f:
    #accept arg from command line
    path = sys.argv[1]
    # if arg is not exist in @record@.txt, then append it
    cmt= "##############################################################################"
    with open('./logs/%s'%path) as f1:
        #write lines in @record@.txt to array lines
        lines = f1.readlines()  # readlines() returns a list of strings
        #for each lines
        for line in lines:
            f.write('start %s' % line)  # write start line
            f.write(cmt)
            f.write('\n')
            steam = os.popen(line).read()
            #write steam to @batch@.txt
            f.write(steam)
            f.write('end %s#############################################################' % line)  # write end line
            f.write('\n')
        f1.close()



    f.close()