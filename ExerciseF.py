
'''
Praveen Manimaran
CIS 41A   Spring 2020
Exercise F
'''

#Part One - Using a main function, Docstrings
def hello():
    '''
    This function prints Hello World
    '''

    print("Hello World")
    
    
#Part Two - Error Handling

def printListElement(list1, index):
    '''
    This function will print ana element from the list as determined
    by the list index. If the list index is invalid, it will print an
    error message.
    '''
    try:
        print(list1[index])
    except:
        print("Error: bad index number.")
    
# Part Three - How Python function arguments are treated
    
def byVal(arg1):
    print("Original ID of parameter in byVal ", id(arg1))
    arg1 += 7
    print("ID of parameter in byVal after change", id(arg1))
        
    
def byRef(list2):
    print("Original ID of parameter in byRef ", id(list2))
    print("Original ID of parameter's last element in byRef ", id(list2[-1]))
    list2[-1] +=7
    print("ID of parameter in byRef after change ", id(list2))
    print("ID of parameter's last element in byRef after change ", id(list2[-1]))
    
    
def main():
    hello()
    help(hello)
    myList = list(range(0,3))
    printListElement(myList, 3)
    myInt = 3
    print("Original ID of myInt in main is ", id(myInt))
    print("Original ID of myList in main is ", id(myList)) 
    print("Original ID of myList's last element in main is ", id(myList[-1]))
    byVal(myInt)
    byRef(myList)
    print("ID of myInt in main after call to byVal is ", id(myInt))
    print("ID of myList in main after call to byRef is ", id(myList))
    print("ID of myList's last element in main after call to byRef is ", id(myList[-1]))
    print("myInt is now: ", myInt)
    print("myList is now: ", myList)
if __name__ == '__main__':
    main()
    
    
'''

Execution results:
    
Hello World
Help on function hello in module __main__:

hello()
    This function prints Hello World

Error: bad index number.
Original ID of myInt in main is  4359390400
Original ID of myList in main is  4713032432
Original ID of myList's last element in main is  4359390368
Original ID of parameter in byVal  4359390400
ID of parameter in byVal after change 4359390624
Original ID of parameter in byRef  4713032432
Original ID of parameter's last element in byRef  4359390368
ID of parameter in byRef after change  4713032432
ID of parameter's last element in byRef after change  4359390592
ID of myInt in main after call to byVal is  4359390400
ID of myList in main after call to byRef is  4713032432
ID of myList's last element in main after call to byRef is  4359390592
myInt is now:  3
myList is now:  [0, 1, 9]


'''