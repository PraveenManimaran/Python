'''
Praveen Manimaran
CIS 41A   Spring 2020
Exercise B
'''


#String Methods

name = input("Enter a name: ")
print("Uppercase: ", name.upper())
print("String length: ", len(name))
print("4th character: ", name[3])
name2 = name.replace('o', 'x')
print("Replacing O with X: ", name2)
print("Original name: ", name)



#Counting and Finding

print("\n")
quote = "Believe you can and you're halfway there."
print("Number of 'a' characters: ", quote.count("a"))
index1 = quote.find('a')
index2 = quote.find('a',index1+1,len(quote))
index3 = quote.find('a',index2+1,len(quote))
index4 = quote.find('a',index3+1,len(quote))

print("Indexes of all 'a' characters: ", index1, index2, index3, index4)


'''
Execution results:
    
Enter a name: George Washington
Uppercase:  GEORGE WASHINGTON
String length:  17
4th character:  r
Replacing O with X:  Gexrge Washingtxn
Original name:  George Washington


Number of 'a' characters:  4
Indexes of all 'a' characters:  13 16 28 32

'''