
#Andrew Paquin
#P3LAB
#2 OCT 2026
#Create a program that will calculate the most efficient way to make change for a given amount of money using the least number of coins possible.

print('Welcome to the Change Calculator!') #Simple greeting to the user

print()

#Use integer division and modulus to calculate the number of coins needed for each denomination
amount = float(input("Enter the amount of money (in dollars): $")) #Prompt user for input of amount of money



cents =round(amount * 100) #Converts value to an integer.


#Determines how many dollars are needed
num_dollars = cents // 100 #Calculates number of dollars
change = cents - (num_dollars * 100)

#Calculates remaining change after dollars are taken out
num_quarters = change // 25 #Calculates number of quarters
change = change - (num_quarters * 25)

num_dimes = change // 10 #Calculates number of dimes
change = change - (num_dimes * 10) #Calculates remaining change after dimes are taken out

num_nickels = change // 5 #Calculates number of nickels
change = change - (num_nickels * 5) #Calculates remaining change after nickels are taken out

num_pennies = change #Calculates number of pennies

if num_dollars > 0: #Check if there are any dollars to display
    if num_dollars == 1: #Check if there is only one dollar to display
        print(f"{num_dollars} dollar") #Display singular dollar
    else:
        print(f"{num_dollars} dollars") #Display plural dollars

if num_quarters > 0: #Check if there are any quarters to display
    if num_quarters == 1: #Check if there is only one quarter to display
        print(f"{num_quarters} quarter") #Display singular quarter
    else:
        print(f"{num_quarters} quarters") #Display plural quarters

if num_dimes > 0: #Check if there are any dimes to display
    if num_dimes == 1: #Check if there is only one dime to display
        print(f"{num_dimes} dime") #Display singular dime
    else:
        print(f"{num_dimes} dimes") #Display plural dimes

if num_nickels > 0: #Check if there are any nickels to display
    if num_nickels == 1: #Check if there is only one nickel to display
        print(f"{num_nickels} nickel") #Display singular nickel
    else:
        print(f"{num_nickels} nickels") #Display plural nickels

if num_pennies > 0: #Check if there are any pennies to display
    if num_pennies == 1: #Check if there is only one penny to display
        print(f"{num_pennies} penny") #Display singular penny
    else:
        print(f"{num_pennies} pennies") #Display plural pennies

if change == 0:
    print("No change.")

