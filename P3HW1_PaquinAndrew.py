#Andrew Paquin
#11 OCT 2026
#P3HW1
#Fix/Debug code exercise


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

#add "round""float" or decimal inputs fail in output

mod_1 = round(float(input('Enter grade for Module 1: ')), 1)
mod_2 = round(float(input('Enter grade for Module 2: ')), 1)
mod_3 = round(float(input('Enter grade for Module 3: ')), 1)
mod_4 = round(float(input('Enter grade for Module 4: ')), 1)
mod_5 = round(float(input('Enter grade for Module 5: ')), 1)
mod_6 = round(float(input('Enter grade for Module 6: ')), 1)

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# determine lowest, highest, sum, and average for grades
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

print('----------------Results----------------')
print(f'Lowest Grade: {low:.1f}')
print(f'Highest Grade: {high:.1f}')
print(f'Sum of Grades: {total:.1f}')
print(f'Average Grade: {avg:.2f}')
print('--------------------------------------')

# determine letter grade for average
if avg >= 90:
    letter_grade = 'A'
elif avg >= 80:
    letter_grade = 'B'
elif avg >= 70:
    letter_grade = 'C'
elif avg >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f'Your grade is: {letter_grade}')




