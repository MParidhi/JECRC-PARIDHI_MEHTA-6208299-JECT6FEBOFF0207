class Car:
    #Below variablea are known as "Properties/States/Members"
    wheelers=4
    engine='Petrol'
    base_speed='40kmph'
    max_speed='120kmph'
    gears=4
    
    
    def __init__(self, air_bags, security, base_budget, varient, total_sale):
        self.air_bags=air_bags
        self.security=security
        self.varient=varient
        self.base_budget=base_budget
        self.total_sale=total_sale
    
TATA=Car(True, 'Level 5', '2L', 12, 100000)
mahindra=Car(True, 'Level 4', '4L', 20, 250000)
    
# TATA=Car()
# TATA.engine=['Petrol','Diesel','EV'] #modification through object
# TATA.air_bags=True
# TATA.no_of_air_bags=4
# TATA.base_budget='2L'
# TATA.no_of_varient=12
##To add 5 new properties, we have to write 5 lines of code, So we will user constructor
## constructor(__init__) --> initialize the state of an object i.e to add
## __init__     --> it is magic method of the constructor

'''
class ClassName:
    properties
    
    def __init__(self, arg1,arg2.....argn):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg2
        .
        .
        .
        self.argn = argn
'''


    
    


