#Andrew Paquin
#27 OCT 2026
#P3HW2
#Salary Calculator with loops

#request employee information
name = input("Enter employee name or 'done' to terminate: ")

#create accumulator variables for overtime, regular pay, gross pay and employee count
overtimepay_total = 0
regularpay_total = 0
grosspay_total = 0
employee_count = 0

while name != 'done':
    # Add employee count plus one
    employee_count += 1
    # Ask for employee info
    hours = float(input('How many hours did ' + name + ' work?: '))
    rate = float(input('What is ' + name + '\'s hourly pay rate?: '))



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

    # accumulate totals
    overtimepay_total += overtime_pay
    regularpay_total += regular_pay
    grosspay_total += gross_pay

    # display results
    print("-----------------------------------")
    print(f'Employee Name:' , name)
    print(f'{"Hours Worked ":<15}{"Pay Rate ":<12}{"OverTime Hours ":<17}{"Overtime Pay ":<15}{"Regular Pay ":<15}{"Gross Pay ":<15}')
    print("---------------------------------------------------------------------------------------")
    print(f'{hours:<15}{rate:<12}{overtime_hours:<17}{"$" + str(overtime_pay):<15}{"$" + str(regular_pay):<15}{"$" + str(gross_pay):<15}')


    name = input("Enter employee name or 'done' to terminate: ")
print()

print("Total number of employees entered:", employee_count)
print("Total amount paid for overtime: $", format(overtimepay_total, ',.2f'))
print("Total amount paid for regular hours: $", format(regularpay_total, ',.2f'))
print("Total amount paid in gross: $", format(grosspay_total, ',.2f'))