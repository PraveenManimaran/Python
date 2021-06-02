'''
Praveen Manimaran
CIS 41A   Spring 2020
Exercise E Script1
'''

scifi = ["Alien", "Solaris", "Inception", "Moon"]
comedy = ["Borat", "Idiocracy", "Superbad", "Bridesmaids"]

for x in range(0,3):
    movie = input("Please enter a movie title: ")
    if movie in scifi:
        print(movie, " is a scifi movie")
    elif movie in comedy:
        print(movie, " is a comedy movie")
    else:
        print("Sorry, I don't know what kind of movie ", movie, " is.")
    
'''
Execution results:

Please enter a movie title: Moon
Moon  is a scifi movie

Please enter a movie title: Superbad
Superbad  is a comedy movie

Please enter a movie title: Dunkirk
Sorry, I don't know what kind of movie  Dunkirk  is.

'''
    