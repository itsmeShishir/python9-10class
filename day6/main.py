# class Student:
#     def __init__(self,name, age):
#         self.name = name
#         self.__age = age
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self, age):
#         self.__age = age

# # object one
# obj1 = Student("Hari", 26)
# print(obj1.name)
# obj1.name = "shyam"
# print(obj1.name)
# print(obj1.set_age(26))
# print(obj1.get_age())

# inheritance

# class Parent:
#     def greet(self):
#         print("this is parent ")

# # child class
# class ChildClass(Parent):
#     def greet(self):
#         super().greet()
#         return "this is from the child class"

# # 
# obj = ChildClass()
# print(obj.greet())

#poly
class Parent:
    def greet(self):
        print("this is parent ")

# child class
class ChildClass(Parent):
    def greet(self, *args, **kwargs):
        print("this is from the child class")

# 
obj = ChildClass()
obj.greet()


# wap create a atm code you already have pin number and amount of 20000 and your pin is 4443
# at first ask the user for the pin number if the pin is correct then ask the user with 4 options 
# 1st. fast withdrawl, 2nd cash withdrawl , 3rd ma total amount, 4th cancel
# user will select this option and so as follow 