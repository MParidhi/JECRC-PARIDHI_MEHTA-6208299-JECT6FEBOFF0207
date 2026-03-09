'''
lambda(Anonymous Function):
    1. Lambda is a keyword, which is used to create anonymous function
    2. For calling the lambda function, we can store the address of lambda inside a variable. By invoking the var_name, we can call the function

Syntax:
var_name=lambda args:<exp>
var_name(args) ##Calling the lambda function
'''

##lambda args: <exp>
# result=lambda a,b: a+b ##returns value
# print(result)
# print(result(1,2)) ##-->preferred syntax

# (lambda a,b: print(a+b))(int(input('First Num: ')), int(input('Second Num: ')))

''''
lambda args: <exp_1> if <cond> else <exp_2>
'''

## WAP to find sqaure of a number if it is even
# num=int(input('Enter number: '))
# if num %2 ==0:
#     print(num ** 2)
    
# result=lambda num: print(num ** 2) if num%2 == 0 else None
# result(10)

# (lambda num: print(num ** 2) if num%2 == 0 else None)(int(input('Enter num: ')))


## WAP to find cube of a number if its odd. If even the square
# result=lambda num: print(num ** 2) if num%2 == 0 else print(num ** 3)
# result(3)


## WAP to find whether number is positive, negative or zero
result=lambda num: print('Positive') if num > 0 else print('Negative') if num < 0 else print('Zero')
result(int(input('Enter any number: ')))





























