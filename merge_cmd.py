import os
import sys

# mkdir logs if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# ping 8.8.8.8 -n 1 -w 1 > logs/ping.log 2>&1   #ping google
# ping -c 1 -w 1

# create log file
with open('./logs/@log@.txt', 'w') as f:
    # accept arg from command line
    # argv[0] is the name of the script
    #接收命令行参数
    args = sys.argv[1:]
    for arg in args:
        f.write('START%s' % arg)
        stream = os.popen(arg).read()
        # stop popen if not end in 4 seconds
        # if stream.find('4') == -1:
        #     f.write('STOP%s' % arg)
        #     break
        f.write(stream)
        f.write('END%s' % arg)
        with open('./logs/%s.txt' % arg, 'w') as f1:
            f1.write(stream)
            f1.close()
    f.close()

#create @record@.txt file if not exists
#创建@record@.txt文件，如果不存在
if not os.path.exists("./logs/@record@.txt"):
    with open("./logs/@record@.txt", "w") as f:
        f.write("")
        f.close()
    #open and append @record@.txt
    #打开@record@.txt文件，将sys.argv[1:]写入文件
    #sys.argv[1:]是命令行参数
with open('./logs/@record@.txt', 'a') as f:
    #accept arg from command line
    args = sys.argv[1:]
    for arg in args:
        #if arg is not exist in @record@.txt, then append it
        with open('./logs/@record@.txt') as f1:
            #write lines in @record@.txt to array lines
            lines = f1.readlines()  # readlines() returns a list of strings
            #if arg is not exist in @record@.txt, then append it
            if not arg in lines:
                f.write(arg)
                f.write('\n')
            f1.close()

    f.close()