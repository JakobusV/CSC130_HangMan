#turning this file into a child of main
import main

#set something variable to 5
something = 5

#increment something variable by 1 (now 6)
something += 1

#set something variable's value to a string that stores "this is a string"
something = "this is a string"

#set something variable to a new string that stores "value" (single or double quotes have no distiction)
something = 'value'


#define a method
def action():

    #variables initialized within the scope of the method
    thing = "some property"

    #call print method
    print(thing)
    
    #method in a method
    def anotherAction():
        print("something else")

    #call nested method from above (never below)
    anotherAction()

#call action method
action()

#define a class
class objectDefinition:
    #properties (variables) of the class
    name = None
    age = 26

    #a function that an object can use
    def doAThing(self):
        print("did a thing")

    #constructor method is always defined as __init__
    #python uses "self" to deliberate between variables that the object holds vs variables that are passed in on initialization (similar to java's "this")
    #self must be a parameter of every function within a class
    def __init__(self, name):
        self.name = name
        print(self.name)


#create an object defined by the class
#the parameter is used in the constructor. not as "self", but as "name". "self" just determines object held properties/ variables
newObject = objectDefinition("Luigi")

#have an object use a function that it owns
newObject.doAThing()

#creating a flexable and changable collection of values, a list
listOfNumbers = [1,2,3]
#appending a new value to the end of the list (index 3 will be created as the value 4)
listOfNumbers.append(4)
#print whole list
print(listOfNumbers)
#print index 3 (will be the value 4)
print(listOfNumbers[3])

#creating an unchangable and functionally {key: value} collection of values, a dictionary
dictOfNumbers = {0: 5 , 1: 6 , 2: 7}
#print the key value pairs within the dictionary
print(dictOfNumbers)

#iterate through a collection of values (in this case, through the dictionary described above)
for i in dictOfNumbers:
    #every iteration, append a value from the dictionary to the list using the keys within the dictionary
    #in this dictionary; the keys 0, 1, and 2 are tied to their respective values; 5, 6, and 7. Therefor, when iterating over the keys 0, 1, and 2; the values appended will be 5, 6, and 7
    listOfNumbers.append(dictOfNumbers[i])

#concatinating requires all values to be strings. the str() method converts any value into a string. (you can overide an str within a class by defining an __str__ function within the class, functionally similar to javas toString class method)
print("list of numbers with dictionary of numbers appended: " + str(listOfNumbers))