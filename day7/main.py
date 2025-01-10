# file handling in python
# mode
# r - read mode, 
# w- write mode,
#  a - append mode, 
# r+ - read and write mode
# open file in read mode
file = open('day7/hello.txt', 'r')
print(file.read())

with open('day7/hello.txt', 'r') as file:
    print(file.read())
# open file in write mode
file = open('day7/text1.txt', 'w')
file.write("hello world by narendra")

with open('day7/text1.txt', 'w') as file:
    file.write("hello world by narendra and age is 25 \n")
# open file in append mode
file = open('day7/text1.txt', 'a')
file.write("hello world by narendra \n")

with open('day7/text1.txt', 'a') as file:
    file.write(f" ok done \n")
# open file in read and write mode
file = open('day7/text2.txt', 'r+')
print(file.read())
file.write("hello world by narendra \n")

# delete file in python using os module
import os
print("file deleted process started")
try:
    os.remove('text2.txt')
except FileNotFoundError:
    print("no such file found")
print("file deleted successfully")
# os.remove('day7/text1.txt')
# os.remove('day7/hello.txt')
#finally, except, else and try
