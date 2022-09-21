#5. Write a python program to delete the age property of the user.
class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj=user("sarwar",30)
print(obj.name)

del obj.age
print(obj.age)