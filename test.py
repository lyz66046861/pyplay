import os
import sys

#move library .\pyplay to C:\Users\lenovo-labtop-lyz
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
#sys.path.append(r'C:\Users\lenovo-labtop-lyz\Desktop\pyplay')
#print(sys.path)
print(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
print('__file__:', __file__)
print(os.pardir)
print(os.path.dirname(__file__))
print(os.path.join(os.path.dirname(__file__), os.pardir))
#accept user input
#print('Please input your name:')
#name = input()
#accept arg from command line
arg=sys.argv[1]
# arg = input("ip:")
#ping 192.168.1 from 1-255 by multi thread
# os.system("ping -t %s -n %s" % (arg, 255))
for i in range(1,256):
    os.system("ping  %s.%s -w 1 -n 1" % (arg,i))
#    os.system('ping 192.168.3.1 -n 1 %s' % i)
#    print('ping -n 1 %s' % i)
