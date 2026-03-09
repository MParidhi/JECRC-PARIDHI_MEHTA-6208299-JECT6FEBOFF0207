'''
Encapsulation: It is used to provide security to the data(data means variables/property and methods present inside the class)

How to provide security to the data?
---ANS. To provide security, we have to use access specifiers.
            1. public,
            2. protected(Soft Barrier '_'),
            3. private
            
Access Specifiers
-- It describes who can access the class members(properties and functionalities)
'''

## Example of public access specifier
# class Temp:
#     a,b,*c,d='HELLO'
    
#     def greeting(self):
#         print('Good Afternoon user: ')
        
# class C2(Temp):
#     pass

## Example of protected access specifier
# class Temp:
#     _a = 10 #if in front of any variable single underscore is there it will act as protected and if double underscore then it will become private
#     _b = 'I LOVE PYTHON'
    
# obj=Temp()
# print(obj._b)
# print(obj._a)

## Example of private access specifier
# class Temp:
#     __a=100
    
#     def __status(self):
#         print('Class name is Temp!')
        
# obj =Temp()
# print(obj.__a)
# obj.__status() -->will throw error

'''
How to  access private access specifier
    1. By using syntax
    2. get & set method
    3. By using @property decorator(setter)
'''

## By using Syntax
'''
obj_name/class_name._CN__prop_name/__method_name (Accessing)
Same syntax will be used for Modifying also
obj_name/class_name._CN__MemberName = NewValue (Modifying)
'''

# class Temp:
#     __a=100
    
#     def __status(self):
#         print('Class name is Temp!')
        
# def newMethod():
#     print('New Mtehod')
        
# obj =Temp()
# print(obj._Temp__a) #--Accessing
# print(Temp._Temp__a)
# obj._Temp__status()
# # Temp._Temp__status() --> not running
# obj._Temp__a='0123456789' #--Modifying
# print(obj._Temp__a)
# obj._Temp__status=newMethod
# obj._Temp__status()


## By using get and set
# class Temp:
#     __a=100
    
#     def status(self):
#         print('Class name is Temp!')
        
#     def get(self):
#         print(self.__a)

#     def set(self, new_val):
#         self.__a=new_val
        
        
# obj=Temp()
# obj.get() #100
# obj.set(1)
# obj.get() #1 --> value got over-ridden
# print(obj._Temp__a) #1


## By using @property decorator
class Temp:
    __a=100
    
    @property
    def getter(self): #getter method will act as a property now
        print(self.__a)
        
    @getter.setter
    def set(self, new_val):
        self.__a=new_val
        
obj=Temp()
# obj.getter() #will not get executd as object is not callable
obj.getter #100
# obj.set(10000) #will not get executd as object is not callable
obj.set = 10000
obj.getter #10000-->value get over-ridden
print(obj._Temp__a) #10000