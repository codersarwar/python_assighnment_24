#3. Write a python program to create 2 objects of the user class and assign different values
class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj=user("sarwar",30)
print(obj.name)
print(obj.age)