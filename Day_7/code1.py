class Car:
    #Below variablea are known as "Properties/States/Members"
    wheelers=4
    engine='Petrol'
    base_speed='40kmph'
    max_speed='120kmph'
    gears=4
    
#Below instances are called as objects
TATA=Car()
# ##To add a new feaeture/property for TATA only ie inside an object--
TATA.air_bags=True
TATA.security='Level 5'

# #For accessing the properties, we have to follow the below syntax
# #obj_name.properties
print('Properties for TATA-----')
print(f'No of Wheelers: {TATA.wheelers}')
print(f'Engine Tyoe: {TATA.engine}')
print(f'Base Speed: {TATA.base_speed}')
print(f'Max Speed: {TATA.max_speed}')
print(f'No of Manual Gears: {TATA.gears}')
#printing new features
print(f'Air bags: {TATA.air_bags}')
print(f'Security: {TATA.security}') ##these two properties will only be shown for TATA not for any other object
print()

mahindra=Car()
print('Properties for Mahindra-----')
print(f'No of Wheelers: {mahindra.wheelers}')
print(f'Engine Tyoe: {mahindra.engine}')
print(f'Base Speed: {mahindra.base_speed}')
print(f'Max Speed: {mahindra.max_speed}')
print(f'No of Manual Gears: {mahindra.gears}')
print()

suzuki=Car()
print('Properties for Suzuki-----')
print(f'No of Wheelers: {suzuki.wheelers}')
print(f'Engine Tyoe: {suzuki.engine}')
print(f'Base Speed: {suzuki.base_speed}')
print(f'Max Speed: {suzuki.max_speed}')
print(f'No of Manual Gears: {suzuki.gears}')
print()

toyota=Car()
print('Properties for Toyota-----')
print(f'No of Wheelers: {toyota.wheelers}')
print(f'Engine Tyoe: {toyota.engine}')
print(f'Base Speed: {toyota.base_speed}')
print(f'Max Speed: {toyota.max_speed}')
print(f'No of Manual Gears: {toyota.gears}')
print()
