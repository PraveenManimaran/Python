'''
Praveen Manimaran
CIS 41A   Spring 2020
Exercise K
'''
import random

list1 = []
for x in range(0,10):
    list1.append(random.randint(1,15))
print(sorted(list1))



def sum_list(numbers):
    sum = 0
    for x in numbers:
        sum += numbers[x]
        return sum
   
'''

Execution results:

[1, 2, 2, 7, 7, 7, 8, 10, 13, 15]


'''   