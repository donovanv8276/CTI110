###Calcuate your travel expenses###
###20231006###
###CTI-110 P1HW2 - Travel Expense###
###Victor Donovan###

print('This program calculates and displays travel expenses')
spend_budget = int(input('Enter Budget:'))
travel_des = input('Enter your travel destination:')
spend_gas = int(input('How much do you think you will spend on gas?'))
spend_hotel = int(input('Approximately, how much will you need for accomodation\hotel?'))
spend_food = int(input('Last, how much do you need for food?'))

print('------------Travel Expenses------------')
print('location:',travel_des)
print('Initial Budget:',spend_budget)
print('Fuel',spend_gas)
print('Accomodation:',spend_hotel)
print('Food:',spend_food)

print('Remaining Balance:',spend_budget-spend_gas-spend_hotel-spend_food)