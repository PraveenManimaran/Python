
'''
Praveen Manimaran
CIS 41A   Spring 2020
Exercise G
'''

#Part One
def printZenPython():
    firstTwoLines = '''Beautiful is better than ugly.\nExplicit is better than implicit. '''
    fout = open('ZenOfPython.txt', 'wt' )
    fout.write(firstTwoLines)
    fout.close()

    otherTwoLines = '''\nReadability counts.\nIf the implementation is hard to explain, it's a bad idea.'''
    fout = open('ZenOfPython.txt', 'at' )
    fout.write(otherTwoLines)
    fout.close()

    fin = open('ZenOfPython.txt', 'rt' )
    poem = fin.read()
    fin.close()

    print(poem)
    print("")

#Part Two

def csvDict():
    import csv
    
    dict1 = { }
    with open('Cities.csv', 'rt') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            dict1[ (row["City"], row["State"])] = row["Population"]


    for i in dict1:
        print(i[0], i[1], dict1[i])

    city = input("Please enter a city: ")
    state = input("Please enter a state: ")

    for j in dict1:
        if(j[0] == city):
            if(j[1] == state):
                print(city, state, "has a population of ", dict1[j])
            
            
            
            
def main():
    printZenPython()
    csvDict()
    
if __name__ == '__main__':
    main()
    

'''

Execution results:

Beautiful is better than ugly.
Explicit is better than implicit. 
Readability counts.
If the implementation is hard to explain, it's a bad idea.

Athens Georgia 115452
Athens Ohio 23832
Berlin Connecticut 19866
Berlin Wisconsin 5524
Dublin California 46036
Dublin Ohio 41751
Glasgow Connecticut 11951
Glasgow Kentucky 14028
London Kentucky 7993
London Ohio 9904
Milan Illinois 5099
Milan Michigan 5836
Milan Tennessee 7851
Paris Kentucky 8553
Paris Tennessee 10156
Paris Texas 25171
Warsaw Indiana 13559
Warsaw New York 5064

Please enter a city: Dublin

Please enter a state: California
Dublin California has a population of  46036

'''

