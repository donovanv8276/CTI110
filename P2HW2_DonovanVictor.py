###Calcuate your travel expenses###
###20231006###
###CTI-110 P1HW2 - Travel Expense###
###Victor Donovan###

print('This program calculates and displays travel expenses')
spend_budget = float(input('Enter Budget:'))
travel_des = input('Enter your travel destination:')
spend_gas = float(input('How much do you think you will spend on gas?'))
spend_hotel = float(input('Approximately, how much will you need for accomodation\hotel?'))
spend_food = float(input('Last, how much do you need for food?'))

print('------------Travel Expenses------------')
print('location:',travel_des)
print(f'Initial Budget: ${spend_budget:.1f}')
print(f'Fuel: ${spend_gas:.1f}')
print(f'Accomodation: ${spend_hotel:.1f}')
print(f'Food: ${spend_food:.1f}')
print('---------------------------------------')

print('Remaining Balance:',spend_budget-spend_gas-spend_hotel-spend_food)
