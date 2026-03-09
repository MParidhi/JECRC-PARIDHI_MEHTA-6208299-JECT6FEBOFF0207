## INHERITANCE
'''
1. Single level
2. Multi-level
3. Multiple
4. Hierarachical
5. Hybrid
'''

## single Level :- we will have a single parent and child class. Also the properties will be derived only one time.


## Parent Class or, Super Class --> The class FROM which we are goint to derieve the properties
class Parent:
    bank_balance = '54L'

    def __init__(self, members): # parent class constructor
        self.members = members

    def desc(self):
        print('I am the Parent class')


## Child Class or, Sub Class --> the class IN which we are going to derive the properties
class Child(Parent):
    def __init__(self, child_name, *args):
          ## to call the parent class constructor
        self.child_name = child_name  
        super().__init__(args)

## method chaning --> calling parent class's method from inside child class's method 
    def display(self):
        super().desc()    



# obj = Child()    
# print(obj.bank_balance)
# obj.desc() 

obj = Child('Rakesh','Mom', 'Dad')
print(obj.members)
print(obj.child_name)
obj.display()

## constructor Chaining :- calling parent class's constructor from inside child class's constructor is known as constructor chaining.

