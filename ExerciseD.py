'''
Praveen Manimaran
CIS 41A   Spring 2020
Exercise D
'''

#Dictionary basics

fruits_desserts = dict(apple = "sauce" , peach = " cobbler", carrot = "cake", 
                       strawberry = "sorbet", banana = "cream pie")
fruits_desserts["mango"] = "sticky rice"
fruits_desserts["strawberry"] = "shortcake"
del fruits_desserts["carrot"]

print("apple dessert is: ", fruits_desserts["apple"])
print("banana dessert exists: ","banana" in fruits_desserts)
print("pear dessert exists: ","pear" in fruits_desserts)

print(fruits_desserts.keys())
print(fruits_desserts.values())
print(fruits_desserts.items())


#Combining dictionaries

capitols1 = dict(Alabama = "Montgomery", Alaska = "Juneau", Arizona = "Phoenix",
                 Arkansas = "Little Rock", California = "Sacramento")
capitols2 = dict(California = "Sac.", Colorado = "Denver", Connecticut = "Hartford")

capitols1.update(capitols2)

print("Sorted state capitols: ", sorted(capitols1.values()))

#Sets Basics

class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
class2 = {"Sasha","Migel","Tanya","Hiroto","Audry"}
class1.add("John")

print("Students in both classes: ",sorted(class1.intersection(class2)))
print("All students: ", sorted(class1.union(class2)))

print("Sasha is in class1: ", "Sasha" in class1 )


'''
Execution results:

apple dessert is:  sauce
banana dessert exists:  True
pear dessert exists:  False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', ' cobbler', 'shortcake', 'cream pie', 'sticky rice'])
dict_items([('apple', 'sauce'), ('peach', ' cobbler'), ('strawberry', 'shortcake'), ('banana', 'cream pie'), ('mango', 'sticky rice')])
Sorted state capitols:  ['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
Students in both classes:  ['Audry', 'Migel', 'Tanya']
All students:  ['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
Sasha is in class1:  False

'''