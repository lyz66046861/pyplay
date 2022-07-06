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

# accept arg from command line
# arg=sys.argv[1]
# arg = input("ip:")
# ping 192.168.1 from 1-255 by multi thread
# os.system("ping -t %s -n %s" % (arg, 255))
# for i in range(1,256):
#     os.system("ping  %s.%s -w 1 -n 1" % (arg,i))
os.system("awk '/\$1|\$6/{print $1}' /etc/shadow")
str = os.system("awk '/\$1|\$6/{print $1}' /etc/shadow")
#print os.popen(ipconfig) to screen 
#print(os.popen("ipconfig").read())
# arr = os.popen("ipconfig /all").readlines()
# for line in arr:
#     print(line)
print(os.popen("ipconfig /all").read())