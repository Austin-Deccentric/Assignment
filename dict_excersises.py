person = {"first_name": "August", "last_name":"Gee", "age": 29}
for key, value in person.items():
    print(f"{key}: {value}")

fav_numbers = {'august': 293, 'reynolds': 439, 'Gerald': 33}
for name, favorite_nums in fav_numbers.items():
    print(f"{name}: {favorite_nums}")

glossary = {
    'mutation': 'change the state of an object',
    'assign': 'give a variable a value',
    'loop': 'go over an object to access it\'s values',
    'string': 'a sequence of characters',
    'integer': 'a whole number',
    'float': 'a number with a decimal point',
    'boolean': 'a value that is either True or False',
}

for term, definition in glossary.items():
    print(f"{term}: \n\t{definition}")

rivers = {
    'nile': 'Egypt',
    'mississippi': 'USA',
    'amazon': 'Brazil',
}

for river, country in rivers.items():
    print(f"{river}: runs through {country}")

for river in rivers:
    print(river)

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

list_of_poll_participants = ['jen', 'austin', 'rex', 'phil']

for participant in list_of_poll_participants:
    if participant in favorite_languages:
         print(f"{participant.title()}, thank you for taking the poll.")
    else:
        print(f"{participant.title()}, please take the poll.")

list_of_people = [
    {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 30,
        'city': 'Kano'
    },
    {
        'first_name': 'Frank',
        'last_name': 'Onyeka',
        'age': 33,
        'city': 'Jersey'
    },
    {
        'first_name': 'Seth',
        'last_name': 'Rolls',
        'age': 27,
        'city': 'Aba'
    }
]

for person in list_of_people:
    print(f"{person['first_name']} {person['last_name']} is {person['age']} years old and lives in {person['city']}.")

pets = [
    {
        'type_of_pet': 'dog',
        'owner_name': 'Austin'
    },
    {
        'type_of_pet': 'cat',
        'owner_name': 'lillian'
    }
]
for pet in pets:
    print(f"This {pet['type_of_pet']} is owned by {pet['owner_name']}.")

favorite_places = {
    'Rita': ['Paris','Strasburg','Berlin'],
    'lillian': ['Amsterdam', 'Bilbao','Curacao'],
    'seth': ['Enugu','Mumbai','Saint Tropaz'],
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"- {place}")

favorite_numbers = {
    'Rita': [42, 39, 67],
    'lillian': [7, 14, 21],
    'seth': [23, 56, 12],
}
for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")

cities = {
    'Enugu':{
        'country':'Nigeria',
        'population': 2_000_000_000,
        'fact': 'The coal city'
    },
    'Abuja':{
        'country':'Nigeria',
        'population': 2_000_000_000,
        'fact': 'Capital of Nigeria'
    },
    'Lagos':{
        'country': 'Nigeria',
        'population': 2_000_000_000,
        'fact': 'The largest city in Nigeria'
    }
}


for city, info in cities.items():
    print(f"\nCity: {city}")
    print(f"\tCountry: {info['country']}")
    print(f"\tPopulation: {info['population']:,}")
    print(f"\tFact: {info['fact']}")
