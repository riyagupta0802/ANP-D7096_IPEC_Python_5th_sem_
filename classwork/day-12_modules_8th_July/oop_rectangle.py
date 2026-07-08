#Defining a class to perform operations on Rectangle

class Rectangle:
    length=0
    breath=0
    #Method to initialize data
    def initialize(Self,l,b):
        self.length = l
        self.breath= b
    #Method to display data
    def display(self):
        print("-----Rectangle-------")
        print("Length:",self.length, "cm")
        print("breath:",self.breath,"cm")

