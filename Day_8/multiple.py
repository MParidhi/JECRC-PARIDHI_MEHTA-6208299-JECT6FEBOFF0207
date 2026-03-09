'''
Multiple Inheritance 
---> It is a type of inheritance in which the properties will be derived from multiple parent class to 
a single child class
'''

class Parent_1:
    a = 10

class Parent_2:
    b = 100

class Parent_3:
    c = 1000


class Parent_4:
    d = 10000


class Child(Parent_1, Parent_2, Parent_3, Parent_4):
    pass


# obj = Child()
# print(obj.a, obj.b, obj.c, obj.d)

## here can do this like without obj at the time of properties calling , have to make obj if we have to call method
print(Child.a, Child.b, Child.c, Child.d)