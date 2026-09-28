
#Andrew Paquin
#27 September 2026
#P2HW1
#Fancy version P1HW2

print("This program calculates and displays travel expenses") #title explaining program utility/input

print('\v') #spacing for readability

budget =(input("Enter budget: ")) #user input for budget
print()
destination =(input("Enter your travel destination: ")) #user input for destination
print()
gas =(input("How much do you think you will spend on gas? ")) #user input for gas
print()
hotel =(input("Approximately, how much will you need for accomodations/hotel? "))
print()
food =(input("Lastly, how much do you think you will need for food? ")) #user input for food
remaining_balance = int(budget) - (int(gas) + int(hotel) + int(food)) #calculating remaining balance
print('\v') #spacing for readability

text = "Travel Expenses"
print(f"{text:-^40}") # Centers 'Travel Expenses' with '-' as the fill character


print(f"{'Location:':<20}{destination:>20}")
print(f"{'Initial Budget:':<20}{f'${float(budget):.2f}':>20}")
print(f"{'Fuel:':<20}{f'${float(gas):.2f}':>20}")
print(f"{'Accommodation:':<20}{f'${float(hotel):.2f}':>20}")
print(f"{'Food:':<20}{f'${float(food):.2f}':>20}")
print("----------------------------------------")
print()
print(f"{'Remaining Balance:':<20}{f'${float(remaining_balance):.2f}':>20}")



print("----------------------------------------")
print('\v')
print("Remaining Balance: ${:<20.2f}".format(float(remaining_balance))) #displaying remaining balance
