'''
Praveen Manimaran
CIS 41A   Spring 2020
Exercise E Script2
'''

for x in range(10, -1, -2):
    print(x)


movies = {"The Wizard of Oz" :1939, "The Godfather" : 1972, "Lawrence of Arabia" : 1962,
              "Ranging Bull" : 1980}


for film in sorted(movies):
    print(film, "was made in ", movies[film])


'''
Execution results:

10
8
6
4
2
0
Lawrence of Arabia was made in  1962
Ranging Bull was made in  1980
The Godfather was made in  1972
The Wizard of Oz was made in  1939

'''

