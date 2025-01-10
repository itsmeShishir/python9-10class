
# #oop -> object oriented programming 
# # -> class , object, encapsulation, inheritance, abstraction, polymorphish
# # class -> constructor and methods

# class abc:
#    c=11

#     #constructon
#    def __init__(self, a, b):
#        self.a = a
#        self.b = b

#     #method
#    def hello(self,name):
#        print( name, self.c)
#    @classmethod
#    def clsmethods(cls):
#         print(cls.c)
#    @staticmethod
#    def noself():
#     print("hello no instance and clss mothods") 

# abcd =abc(100,200)
# print(abcd.a)
# print(abcd.b)
# abcd.hello("shsihir")
# abcd.clsmethods()
# abcd.noself()

class Student:
   rollnumber = 10
   def __init__(self, name, gender, age):
      self.name = name
      self.gender = gender,
      self.age = age
    
   def details(self):
      print(self.name, self.gender, self.age) 
    
   @classmethod
   def oneClass(cls):
      print(cls.rollnumber)

   @staticmethod
   def StaticOne():
      print("about student")

newstudent = Student("hari", "male", 27)
newstudent.details()
newstudent.oneClass()
newstudent.StaticOne()
 

