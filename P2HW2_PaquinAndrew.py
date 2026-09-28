
#Andrew Paquin
#27 September 2026
#P2HW2
#Test grade program

#insert relevant grades into a list
grades = [65.5, 88, 78.5, 90, 61, 92]
#create a list of modules, append grades and modules to combine list contents
modules = ["Module 1", "Module 2", "Module 3", "Module 4", "Module 5", "Module 6"]
module1 = float(input("Enter grade for Module 1: "))
grades.append(module1)
module2 = float(input("Enter grade for Module 2: "))
grades.append(module2)
module3 = float(input("Enter grade for Module 3: "))
grades.append(module3)
module4 = float(input("Enter grade for Module 4: "))
grades.append(module4)
module5 = float(input("Enter grade for Module 5: "))
grades.append(module5)
module6 = float(input("Enter grade for Module 6: "))
grades.append(module6)

print()
# Calculate grade statistics 
min_value = min(grades)
max_value = max(grades)
sum_value = sum(grades)
avg_value = sum_value / len(grades)
#ensure results are displayed in a formatted table with proper spacing
print("-------------Results------------")
print(f"Lowest Grade: {min_value:>10.1f}")
print(f"Highest Grade: {max_value:>9.1f}")
print(f"Sum of Grades: {sum_value:>10.1f}")
print(f"Average: {avg_value:>16.2f}")
print("--------------------------------")