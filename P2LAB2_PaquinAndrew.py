
#Andrew Paquin
#27 September 2026
#P2LAB2
#Using Dictionaries

cars = {'Camaro': 18.21, 'Prius': 52.36, 'Model S': 110.0, 'Silverado': 26}

#Get keys from dictionary
cars_keys = cars.keys()
print(cars_keys)
print(*cars_keys, sep = ", ")

#Ask user to enter a car model
model = input("Enter a vehicle to see it's mpg: ")
print()

#Get the MPG for the entered model
mpg = cars.get(model)
if mpg is not None:
    print(f"The {model} gets {mpg} mpg")
else:
    print(f"Model {model} not found in the dictionary.")

print()

#ask user how many miles they will drive the model
miles = float(input(f"How many miles you will drive the {model}?: "))
print()

#calculate the amount of gas needed
gas_needed = miles / mpg
print(f"{gas_needed:.2f} gallons of gas are needed to drive the {model} {miles} miles.")