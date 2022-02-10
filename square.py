import sys
from typing import Type

class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passengers(self,name):
        if len(self.passengers) != self.capacity:
            self.passengers.append(name)
            print(f'added {name}')
        else:
            print("full")

flight1 = Flight(5)

flight1.add_passengers('marie')
flight1.add_passengers('marie')
flight1.add_passengers('marie')
flight1.add_passengers('marie')
flight1.add_passengers('marie')
flight1.add_passengers('marie')


print(flight1.passengers)





people = [
    {"Name":"harry","house":"yomama"},
    {"Name":"fart","house":"Gryffindor"},
    {"Name":"yas","house":"wow"}

]

def f(person): #sorts by alphabetical order by each persons name
    return person["Name"]

people.sort(key=lambda person: person["Name"]) #lambda function
print(people)





x = input('x')
y = input('y')

try:
    result = x/y
except ZeroDivisionError:
    print('Error: cannot divide by 0')
    sys.exit(1)
except TypeError:
    print('wrong value')
    sys.exit(1)

print(f"{x} / {y} = {result}")
