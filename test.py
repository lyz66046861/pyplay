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
