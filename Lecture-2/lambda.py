people = [
    {"name": "Harry", "house": 'Gryffindor'},
    {"name": "Cho", "house": 'Ravenclaw'},
    {"name": "Draco", "house": 'Slytherin'}
]

""" 
def sortByName(person):
    return person["name"]  

people.sort(key = sortByName)
"""

people.sort(key = lambda person : person["name"])
print(people)