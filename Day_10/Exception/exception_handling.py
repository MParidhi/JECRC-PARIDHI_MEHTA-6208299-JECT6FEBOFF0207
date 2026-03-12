'''
Exception Handling
--Unauthorized event-->it will never take permission from us and we will not understand why nd when it will occur
--Due to this, the flow of exceution of the prg will stop
--It will never execute the further code

Error-----Error Name
          Reason
          Line No.
          
Error in pink aur purple color--->It is known as exception
Error in red--->Serious issue i.e actual error
Sometimes a warning in purple color--->It is called warning. Here the code will be exceuted but a warning will be raised

Syntax error
--We can handle all the errors except syntax error

try: We will put the problem statement here i.e. Block of code due to which we might get error
else: If we get error in any line of try block, it will not hit error it will directly move to else block and will execute it and ignore the error of try block and print the output of the alternative block i.e else block if the code is correct (if incorrect--> it will give error)
      It is an alternative of try block. If else block is executed correctly then no need of except block
except: If error in both try and else block, we will use except block.
        We put the actual solution for the error. Solution here means resolution for error prone code
        Due to except block, we can prevent the unauthorized events(errors)
finally: After getting error or after resolution, forcefully if we want to execute any particular block of code, then we use finally block
'''

'''
Exception Handling Approach
    1. Specific Exception Handling
    2. Generic Exception Handling
    3. Default Exception Handling
'''

'''  
Specific Exception Handling
    --- If we are aware of the error or exception, then we can go with Specific
    try:
        problem
        statement
    except ErrorName:
        resolution/
        solution code
'''

# n1,n2=21,0
# #print (n1/n2) ##error-->will not get execute further

# try:
#     ##problem statement
#     result=n1/n2
#     print(result)
    
# except ZeroDivisionError:
#     ##solution code
#     print('Please do not choose zero a second number')

# print('Code after try except-01')
# print('Code after try except-02')
# print('Code after try except-03')


# try:
#     a,b,c=1,2
# except ValueError:
#     print('For performing MVC, number of variables should be equals to number of values!')
# # print(a,b,c)  ##NameError: name 'a' is not defined --> so we will put it in another try-except block

# try:
#     print(a,b,c)
# except NameError:
#     print('Identifiers are not there in the memory')
    
## But it is not possible to remember all the child class exception name so we go with generic

'''
Generic Exception Handling
    ---It is a type of exception handling approach in which there is no need to pass any particular exception class name. Instead of we can use parent "exception" class called "Exception"
'''

# try:
#     a,b,c=1,2
# except Exception:
#     print('For performing MVC, number of variables should be equals to number of values!')

# try:
#     print(a,b,c)
# except Exception:
#     print('Identifiers are not there in the memory')
    
## Using generic, we cant handle keyboard interruption
# import time
# try:
#     while True:
#         print(time.time())
# except Exception:
#     print('Loop got stopped') ##Loop will get exceute infinite times but if we stop it then we will get KeyboardInterrupt error

'''
Default Exception Handling
    ---It is a type of exception handling in which we can handle all types of errors or exceptions(incliding Keyboard Interrupt) except "Syntax error" (and also software problems..)
'''

import time
try:
    while True:
        print(time.time())
except:
    print('Loop got stopped') ##will not give any error, will print loop got stopped..