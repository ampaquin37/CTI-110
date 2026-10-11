#Andrew Paquin
#11 OCT 2026
#P3HW2
#Salary Calculator

#request employee information
name = input('Enter employee name: ')
hours = float(input('Enter number of hours worked: '))
rate = float(input('Enter hourly pay rate: '))

# evaluate overtime 
if hours > 40:
    # calculate overtime
    overtime_hours = hours - 40
    # calculate overtime pay
    overtime_pay = overtime_hours * (rate * 1.5)
    # calculate regular pay
    regular_pay = 40 * rate
    # calculate gross pay
    gross_pay = regular_pay + overtime_pay
else:
    overtime_pay = 0
    overtime_hours = 0
    regular_pay = hours * rate
    gross_pay = regular_pay

# display results
print("-----------------------------------")
print(f'Employee Name:' , name)
print(f'{"Hours Worked ":<15}{"Pay Rate ":<12}{"OverTime Hours ":<17}{"Overtime Pay ":<15}{"Regular Pay ":<15}{"Gross Pay ":<15}')
print("---------------------------------------------------------------------------------------")
print(f'{hours:<15}{rate:<12}{overtime_hours:<17}{"$" + str(overtime_pay):<15}{"$" + str(regular_pay):<15}{"$" + str(gross_pay):<15}')