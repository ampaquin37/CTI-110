 # Andrew Paquin
 # 13 SEPTEMBER 2026
 # P1HW2
 # Travel expense python program

print("This program calculates and displays travel expenses") #title explaining program utility/input

print('\v') #spacing for readability

budget =(input("Enter budget: ")) #user input for budget
destination =(input("Enter your travel destination: ")) #user input for destination
gas =(input("How much do you think you will spend on gas? ")) #user input for gas
hotel =(input("Approximately, how much will you need for accomodations/hotel? "))
food =(input("Lastly, how much do you think you will need for food? ")) #user input for food
remaining_balance = int(budget) - (int(gas) + int(hotel) + int(food)) #calculating remaining balance
print('\v') #spacing for readability

print("------------Travel Expenses------------") #title for output

print("Location: ",destination) #displaying destination
print("Initial Budget: ",budget) #displaying budget
print('\v') #spacing for readability
print("Fuel: ",gas) #displaying gas
print("Accomodation: ",hotel) #displaying hotel
print("Food: ",food) #displaying food
print('\v') #spacing for readability
print("Remaining Balance: ",remaining_balance) #displaying remaining balance



