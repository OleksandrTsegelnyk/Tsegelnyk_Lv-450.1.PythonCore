#You were camping with your friends far away from home, but when it's time to go back, 
# you realize that you fuel is running out and the nearest pump is 50 miles away! 
# You know that on average, your car runs on about 25 miles per gallon. 
# There are 2 gallons left. Considering these factors, 
# write a function that tells you if it is possible to get to the pump or not. 
# Function should return true if it is possible and false if not.

# distance_to_fuel = int(input("How many miles to the gasstantion? "))
# fuel_inthe_tank = int(input("How many fuel to ypu have in the tank?"))
# gallon_per_mile = int(input("Input avarage uses of fuel"))
################################################
#First way

# def fuel_calculator(distance_to_fuel, fuel_inthe_tank, gallon_per_mile):
#     if (distance_to_fuel / gallon_per_mile) == fuel_inthe_tank:
#         print("You will made it")
#     elif (distance_to_fuel / gallon_per_mile) < fuel_inthe_tank:
#         print("You will made it")
#     else:
#         print("You shouldn't do it")
    
# print(fuel_calculator(10,2,50))

##########################################################################
# second way
distance_to_fuel = int(input("How many miles to the gasstantion? "))
fuel_inthe_tank = int(input("How many fuel to ypu have in the tank?"))
gallon_per_mile = int(input("Input avarage uses of fuel"))

def fuel_calculator():
    if (distance_to_fuel / gallon_per_mile) == fuel_inthe_tank:
        return True
    elif (distance_to_fuel / gallon_per_mile) < fuel_inthe_tank:
        return True
    else:
        return False
    
print(fuel_calculator())