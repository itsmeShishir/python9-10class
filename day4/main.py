print("this is inbuild function")
def firstLetter():
    print("Hello")

firstLetter()
firstLetter()

#parameter -> argument 
def hello(abc):
    print(f"this is hello page {abc}")

hello("hi")
hello(4)

def hellohi(name, age = 28):
    return f"hello hi {name} and your age is {age}"

print(hellohi(age=27, name="hari"))
print(hellohi(name="sita", age= 40))

def listname(*args):
    for name in args:
        print(f"Hello {name}")

listname("hari", "sita", "laxman")

def kwargss(**info):
    for keys, values in info.items():
        print(f"{keys}: {values}" )

kwargss(name="hari", age="27", isMale= True, email="hari@gmail.com")


#oop -> object oriented programming 
# -> class , object, encapsulation, inheritance, abstraction, polymorphish
# class -> constructor and methods

class abc:
   c=11

    #constructon
   def __init__(self, a, b):
       self.a = a
       self.b = b

    #method
   def hello(self,name):
       print( name, self.c)
   @classmethod
   def clsmethods(cls):
        print(cls.c)
   @staticmethod
   def noself():
    print("hello no instance and clss mothods", c) 

abcd =abc(100,200)
print(abcd.a)
print(abcd.b)
abcd.hello("shsihir")
abcd.clsmethods()
abcd.noself()