 # CTI-110
   # P2HW2 - Module Grades
   # Victor Donovan
   # 02NOV2023
   #

Module_grades=[]
Module_1=float(input('Module 1:'))
Module_3=float(input('Module 3:'))
Module_4=float(input('Module 4:'))
Module_5=float(input('Module 5:'))
Module_6=float(input('Module 6:'))

Module_grades=(Module_1,Module_2,Module_3,Module_4,Module_5,Module_6)

Sum_of_grades=(Module_1+Module_2+Module_3+Module_4+Module_5+Module_6)

Grade_average=(Sum_of_grades/6)

print(------------Results------------)
print(f'Lowest Grade:{min(Module_grades)}')
print(f'Highest Grade:{max(Module_grades)}')
print('Sum of Grades:'Sum_of_grades)
print('Average:'Grade_average)
print(----------------------------------------------)