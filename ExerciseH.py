'''
Praveen Manimaran
CIS 41A   Spring 2020
Exercise H
'''
#Part 1 - A Basic Class - State Data
class StateData:
    def __init__(self, name, abbreviation, region, population ):
        self.name = name
        self.abbreviation = abbreviation
        self.region = region
        self.population = population
    def __str__(self):
        return self.name
    def displayState(self):
        print(self.name, "(", self.abbreviation, ") is in the", self.region,
              "and has population of", self.population)
            
s1 = StateData("California", "CA", "West", 39250000)
print(s1)
s1.displayState()
print("")

#Part 2 - Different ways of working with Attributes

class StateData2:
    def __init__(self, name):
        self.name = name
    def setRegion(self, region):
        self.region = region
    def getRegion(self):
        return self.region

s2 = StateData2("Califronia")
s2.setRegion("West")
s2.pop = 32950000
print(s2.name)
print(s2.getRegion())
print(s2.region)
print(s2.pop)
print()

#Part 3 - Data Hiding
class StateData3:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"
test = StateData3()
print(test.public)
print(test._protected)
print(test.__private)

'''

Execution results:

California
California ( CA ) is in the West and has population of 39250000

Califronia
West
West
32950000

Public
Protected
Traceback (most recent call last):

  File "/Users/praveenmanimaran/Desktop/Python Programs/ExerciseH.py", line 52, in <module>
    print(test.__private)

AttributeError: 'StateData3' object has no attribute '__private'

'''

