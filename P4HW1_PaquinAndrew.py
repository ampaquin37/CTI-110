
#Andrew Paquin
#27 OCT 2026
#P4HW1
#Test grade program using loops


#Ask user to input the number of scores they would like to enter.
num_scores = int(input("How many scores would you like to enter? "))

#create an informative list
scores_list = []

#Start a counter
count = 0

#use while loop until number of desired scores is entered
while count < num_scores:
    grade = float(input(f"Enter score # {count + 1}: "))
    

    #if score is invalid notify operator
    while grade < 0 or grade > 100:
        print("INVALID score entered!!!!")
        print("Score should be between 0 and 100.")
        grade = float(input(f"Enter score # {count + 1} again: "))

    #add scores to list, ensure this block remains in the loop
    scores_list.append(grade)
    count += 1

#add space for separation of input and output
print()

print("------------Results------------")

#find the lowest score
lowest_score = min(scores_list)
print(f"Lowest score: {lowest_score}")

#remove the lowest score from the list and display
scores_list.remove(lowest_score)
print(f"Modified list: {scores_list}")

#calculate the average of the modified list
average_score = sum(scores_list) / len(scores_list)
print(f"Scores Average: {average_score:.2f}")

# Determine the letter grade
if average_score >= 90:
    letter_grade = "A"
elif average_score >= 80:
    letter_grade = "B"
elif average_score >= 70:
    letter_grade = "C"
elif average_score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

#display letter grade
print(f"Grade: {letter_grade}")

print("----------------------------")





