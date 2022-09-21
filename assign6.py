#6. Write a python program to create 3 user objects and find the youngest of all.
class user:
    def __init__(self,name,age):
        self.name = name
        self.age = age
print("old")
obj=user("sarwar",30)
print(obj.name)
print(obj.age)

print("young")
obj1=user("sar",20)
print(obj1.name)
print(obj1.age)
print("medium")
obj2=user("sarwa",25)
print(obj2.name)
print(obj2.age)