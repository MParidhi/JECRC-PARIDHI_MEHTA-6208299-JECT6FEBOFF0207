'''
Abstraction: Hiding the internal implementation and showing only the functionality to the end user.

Abstract Method:
--If a method or a function consist of only declaration not definition then it will be called as "abstract method"
def def_name():
    pass
    
Abstract Class:
--If a class consist of atleast one abstract method then it will be called as "abstract class"

Concret Class:
--If a class does not have a single abstract method then it will be called as "concret class"

abc: Module
ABC: Abstract Base Class
'''

from abc import ABC, abstractmethod

class ATM(ABC): #abstract method is present inside ATM class hence it will be called abstract class
    @abstractmethod
    def generate_pin(self):
        pass
    
    @abstractmethod
    def forgot_pin(self):
        pass
    
    @abstractmethod
    def check_balance(self):
        pass
    
    @abstractmethod
    def withdraw(self):
        pass
    
    @abstractmethod
    def deposit(self):
        pass
    
## oyu cannot creae any object from abstract class

class SBI_ATM(ATM):
    def generate_pin(self):
        print('It is used to generate ATM pin')
        
    def forgot_pin(self):
        print('Not able to remember the pin then Forgot Pin!')
        
    def check_balance(self):
        print('No balance is there in your account :(')
        
    def deposit(self):
        print('Save your money by giving it to me')
    
    def withdraw(self):
        print('Do not withdraw the money. Please!')
        
#Now each and every method has definition and the class SBI_ATM will be called concret class

obj=SBI_ATM()
obj.generate_pin()
obj.forgot_pin()
obj.check_balance()
obj.deposit()
obj.withdraw()