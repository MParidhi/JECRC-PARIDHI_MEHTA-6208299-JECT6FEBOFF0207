'''
raise-->Keyword which helps us to thrown an error in between a program

Exception Creation
    1. Custom Exception(raise)
    2. User-defined Exception(raise)
    3. Assertion Exception(assert)
'''

'''
Custom Exception
--Here we use pre-built exception classes according to our requirement. We will never create new classes
  
  raise ValueError('message')
  
  #so whenever error will occur, it will look like:-->ValueError: message  
'''

# num=17
# if num>=18:
#     print('You are eligible to vote and drive')
# else:
#     raise ValueError('Age should be greater than or equals to 18!') ##you can use any of the class name eg instead of valu error you can use NameError

'''
User-defined Exception
--It is a type of exception in which we can create our own exception classes based upon our own requirement. We can also provide names to those classess according to the user cases

class MyException(Exception):
    pass
raise MyException('message')
'''

# class MyException(Exception):
#     pass

# # raise MyException('This is my exception class')
# n1, n2 = 10, 0

# if n2==0:
#     raise MyException('Second num cannot be Zero')
# else:
#     print(n1/n2)

'''
Assertion Exception
--It can be created by using one keyword "assert"

assert <condition>, print('ERROR')   #will print error if condition is not satisfies
print(output) #will print output if condition is true
'''

s=input('Enter a string: ')
assert s==s[::-1], print('It is not a palindromic string')
print('It is a palindromic string')