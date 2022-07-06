import os
import sys

# mkdir logs if not exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# create log file
with open('./logs/@log@.txt', 'w') as f:
    # accept arg from command line
    # argv[0] is the name of the script
    #接收命令行参数
    args = sys.argv[1:]
    for arg in args:
        f.write('START%s' % arg)
        f.write('\n')
        stream = os.popen(arg).read()
        print(stream)
        f.write(stream)
        f.write('END%s' % arg)
        f.write('\n')
        #escape / in arg
        arg = arg.replace('/', '_')
        try:
            with open('./logs/%s.txt' % arg, 'w') as f1:
                f1.write(stream)
                f1.close()
        except Exception as e:
            print(e)
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

#delete duplicate line in @record@.txt
#删除@record@.txt文件中的重复行
with open('./logs/@record@.txt', 'r') as f:
    lines = f.readlines()  # readlines() returns a list of strings
    lines = list(set(lines)) # remove duplicate lines
    with open('./logs/@record@.txt', 'w') as f1:
        # for line in lines:
        #     f1.write(line)
        f1.write(''.join(lines))
        f1.close()
    f.close()