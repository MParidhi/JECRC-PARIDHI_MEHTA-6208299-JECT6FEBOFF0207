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
        
    @classmethod
    def update_gears(cls,new_gears):
        cls.gears=new_gears
        print(f'No of Gears: {cls.gears}') ##this modification is done wrt class so it will reflected on all the object
        
    ##Functionalities
    def display_properties(self):
        print({
            'wheelers': self.wheelers,
            'engine': self.engine,
            'base_speed': self.base_speed,
            'max_speed': self.max_speed,
            'gears': self.gears,
            'air_bags': self.air_bags,
            'security': self.security,
            'base_budget': self.base_budget,
            'varient': self.varient,
            'total_sale': self.total_sale
        })
        
    ##Updating
    def update_base_speed(self, new_speed):
        self.base_speed=new_speed
        print(f'New Base Speed: {self.base_speed}') ##this modification is done wrt object so it will reflected on only that particular object calling this function
        
    def update_max_speed(self, new_speed):
        self.max_speed=new_speed
        print(f'New Max Speed: {self.max_speed}')
        
print("Properties before updation")       
TATA=Car(True,'Level 5','2L', 12, 100000)
TATA.display_properties()

print("Properties after updation")
TATA.update_base_speed('60kmph')
TATA.update_max_speed('160kmph')
TATA.display_properties()
