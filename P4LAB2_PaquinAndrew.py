#Andrew Paquin
#27 OCT 2026
#P4LAB2
#Use while/for loops to create a multiplication table for positive integers

#get an integer from the user
#determine if integer is positive or negative
#if the number is positive, display multiplication table (1-12)
#if the number is negative, display "This program does not handle negative numbers"
#prompt user to run program again: if yes, run again; if no, exit program.

run_again = 'yes'

while run_again != "no":

    user_num = int(input("Enter an Integer: "))
    if user_num >= 0:
        #display multiplication for value and range (1-12)
        for item in range(1, 12+1):
            print(f"{user_num} * {item} = {user_num * item}")
    else: 
        print("This program does not handle negative numbers.")

    run_again = input("Would you like to run the program again? ")
#Loop has broken: user entered 'no'

print("Program is ending...")
