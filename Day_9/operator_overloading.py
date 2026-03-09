'''
Operator Overloading: It is a phenomenon of making the operators to work on user-defined data types by invoking respective magic methods.

-- Magic Methods/Dundar: special type of method in which at the starting or at the ending of the method's name double underscore will be there

--Example:
    1. __add__
    2. __sub__
    3. __mul__
    4. __floordiv__
    5. __truediv__
    6. __mod__
    
-- If we do not use operator overloading then what will happen?
ANS-- For using the operators inside user-defined data types we have to use operator overloading

-- Syntax:
    class ClassName:
        def __init__(self, val):
            self.val=val
            
        def __add__(self,ano_obj):
            return self.val + ano_obj.val
    
    obj1=ClassName(val1)
    obj2=Classname(val2)
    print(obj1 + obj2)
'''


class MyDT:
    def __init__(self, val):
        self.val=val
    
    # def __add__(self, ano_obj):
    #     return self.val + ano_obj.val 
    
    # def __sub__(self, ano_obj):
    #     return self.val - ano_obj.val
    
    # def __mul__(self, ano_obj):
    #     return self.val * ano_obj.val
    
    # def __floordiv__(self, ano_obj):
    #     return self.val // ano_obj.val
    
    # def __truediv__(self, ano_obj):
    #     return self.val / ano_obj.val
    
    # def __mod__(self, ano_obj):
    #     return self.val % ano_obj.val
    
    def __str__(self):
        return str(self.val)
    
    def __add__(self, *ano_obj):
        result = self.val
        for i in ano_obj:
            result += i.val
        return MyDT(result)
    
    def __sub__(self, *ano_obj):
        result = self.val
        for i in ano_obj:
            result -= i.val
        return MyDT(result)
    
    def __mul__(self, *ano_obj):
        result = self.val
        for i in ano_obj:
            result *= i.val
        return MyDT(result)
        
    
    # def add(self, *args):
    #     result = self.val
    #     for obj in args:
    #         result+=obj.val
    #     return result
    
    # def sub(self, *args):
    #     result = self.val
    #     for obj in args:
    #         result-=obj.val
    #     return result
    
    # def mul(self, *args):
    #     result = self.val
    #     for obj in args:
    #         result*=obj.val
    #     return result
    
# print(MyDT(10) + MyDT(20))
# print(MyDT(100) - MyDT(20))
# print(MyDT(10) * MyDT(20))
# print(MyDT(100) // MyDT(20))
# print(MyDT(100) / MyDT(20))
# print(MyDT(100) % MyDT(20))
print(MyDT(10) + MyDT(20) + MyDT(20))
print(MyDT(100) - MyDT(20) - MyDT(20))
print(MyDT(10) * MyDT(20) * MyDT(20))
# print(MyDT.add(MyDT(100), MyDT(200), MyDT(300)))
# print(MyDT.sub(MyDT(1000), MyDT(200), MyDT(300)))
# print(MyDT.mul(MyDT(100), MyDT(200), MyDT(300)))
