class MyDataType:
    def __init__(self, val):
        self.val = val

    def __add__(self, ano_obj):
        return self.val + ano_obj.val 

    def __mul__(self, ano_obj):
        return self.val * ano_obj.val    

    ## self.val  
    ## obj -> self.val
    ## ano_obj(obj2) --> obj2.val --> ano_obj.val       

obj1 = MyDataType(10)
obj2 = MyDataType(20)
obj3 = MyDataType(30)
print(10+20)
print(obj1 + obj2)       