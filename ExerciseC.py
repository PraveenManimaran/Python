'''
Praveen Manimaran
CIS 41A   Spring 2020
Exercise C
'''

import copy

list1 = [2, 4.1, 'hello']
list2 = list1
list3 = copy.deepcopy(list1)

print("list1 == list2: ", list1 == list2)
print("list1 == list3: ", list1 == list3 )
print("list2 == list3: ", list2 == list3)

print("list1 is list2: ", list1 is list2)
print("list1 is list3: ", list1 is list3)
print("list2 is list3: ", list2 is list3)

print("list1 ID: ", id(list1))
print("list2 ID: ", id(list2))
print("list3 ID: ", id(list3))

list1.append(8)
list2.insert(1, 'goodbye')
del list3[0]

print("list1 printed:",list1)
print("list2 printed:",list2)
print("list3 printed:",list3)

'''
Execution results:

list1 == list2:  True
list1 == list3:  True
list2 == list3:  True
list1 is list2:  True
list1 is list3:  False
list2 is list3:  False
list1 ID:  4787743552
list2 ID:  4787743552
list3 ID:  4808429152
list1 printed: [2, 'goodbye', 4.1, 'hello', 8]
list2 printed: [2, 'goodbye', 4.1, 'hello', 8]
list3 printed: [4.1, 'hello']

'''

