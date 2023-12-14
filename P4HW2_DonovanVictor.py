# CTI-110
# P4HW2 - Salary
# Victor Donovan
# 10DEC2023
# 

total_regular_pay=0
total_overtime_pay=0
overtime_hours=0
total_gross_pay=0
Employees=0

while True:
    employee_name=input("Enter employee's name or 'Done' to terminate:")
    if employee_name.lower()=='done':
        break
    hours_worked=float(input(f"How many hours did {employee_name} work? "))
    pay_rate=float(input(f"What is {employee_name}'s pay rate? "))

    if hours_worked<=40:
        regular_pay=hours_worked*pay_rate
        overtime_pay=0
    else:
        regular_pay=40*pay_rate
        overtime_hours=hours_worked-40
        overtime_pay=overtime_hours*(pay_rate*1.5)
    gross_pay=regular_pay+overtime_pay

    Employees += 1
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    total_gross_pay += gross_pay

    print('-----------------------------------')
    print('Employee name:',employee_name)
    print('Hours Worked     Pay Rate     Overtime     Overtime Pay     RegHour Pay     Gross Pay')
    print('-------------------------------------------------------------------------------------')
    print(f'{hours_worked:<16.2f}{pay_rate:<16.2f}{overtime_hours:<16.2f}{overtime_pay:<16.2f}{regular_pay:<16.2f}{gross_pay:<16.2f}')


print(f"Total number of employees entered: {Employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_regular_pay:.2f}")
print(f"Total amount paid in gross: ${total_gross_pay:.2f}")
input('press enter to exit')
