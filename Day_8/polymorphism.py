class Temp:

    def sum(self, a, b):
        print(a+b)

    add_two_nums = sum   #monkey patching 

    def sum(self, a, b, c):
        print(a+b+c)

obj = Temp()
obj.add_two_nums(10, 20)  
obj.sum(10, 20, 30)          