#!/bin/python3
# Exercise 6-1 Person
# Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as =first_name=, =last_name=, =age=, and =city=. Print each piece of information stored in your dictionary.

# [[file:../../Notes.org::*Exercise 6-1 Person][Exercise 6-1 Person:1]]
iuser = {"first_name": "kakushi", "last_name": "goto", "age": 36, "city": "tokyo"}

print(f"first_name: {iuser['first_name']}")
print(f"last_name: {iuser['last_name']}")
print(f"age: {iuser['age']}")
print(f"city: {iuser['city']}")
# Exercise 6-1 Person:1 ends here

# Exercise 6-2 Favorite Numbers
# Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

# [[file:../../Notes.org::*Exercise 6-2 Favorite Numbers][Exercise 6-2 Favorite Numbers:1]]
inumbers = {"anna": 24, "kira": 12, "jane": 39, "joan": 45, "justine": 50}
print("Favorite numbers")
for key, val in inumbers.items():
    print(f"{key.title()}: {val}")
# Exercise 6-2 Favorite Numbers:1 ends here

# Exercise 6-3 Glossary
# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# - Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values. 
# - Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (=\n=) to insert a blank line between each word-meaning pair in your output.

# [[file:../../Notes.org::*Exercise 6-3 Glossary][Exercise 6-3 Glossary:1]]
iglossary = {'tupple': 'Unmodifiable list',
             'list': 'Array of objects',
             'comprehension list': 'A list created from a single linefor loop',
             'floating': 'A number with decimals',
             'integer': 'Integer'}

print(f"- tupple: {iglossary['tupple']} \n")
print(f"- list: {iglossary['list']} \n")
print(f"- comprehension list: {iglossary['comprehension list']} \n")
print(f"- integer: {iglossary['integer']} \n")
# Exercise 6-3 Glossary:1 ends here

# Exercise 6-4 Glossary 2
# Now that you know how to loop through a dictionary, clean up the code from [[Exercise 6-3 Glossary][Exercise 6-3]] by replacing your series of =print()= calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.


# [[file:../../Notes.org::*Exercise 6-4 Glossary 2][Exercise 6-4 Glossary 2:1]]
for term, meaning in iglossary.items():
    print(f"- {term.title()}: {meaning} \n")
# Exercise 6-4 Glossary 2:1 ends here

# Exercise 6-5 Rivers
# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# - Use a loop to print a sentence about each river, such as The Nile runs through Egypt  ([[l_code:ex6-5-1][\rightarrow]])
# - Use a loop to print the name of each river included in the dictionary ([[l_code:ex6-5-2][\rightarrow]])
# - Use a loop to print the name of each country included in the dictionary ([[l_code:ex6-5-3][\rightarrow]]).

# <<l_code:ex6-5list>>
# #+name: ex6-5list

# [[file:../../Notes.org::ex6-5list][ex6-5list]]
southAmerica_rivers = {
    'Argentina': 'Paraná',
    'Bolivia': 'Beni',
    'Brazil': 'Amazon'}
# ex6-5list ends here



# #+RESULTS: ex6-5list

# <<l_code:ex6-5-1>>
# #+name: ex6-5-1

# [[file:../../Notes.org::ex6-5-1][ex6-5-1]]
for country, river in southAmerica_rivers.items():
    print(f"The river {river} runs trough {country}")
# ex6-5-1 ends here



# #+RESULTS: ex6-5-1
# : The river Paraná runs trough Argentina
# : The river Beni runs trough Bolivia
# : The river Amazon runs trough Brazil

# <<l_code:ex6-5-2>>
# #+name: ex6-5-2

# [[file:../../Notes.org::ex6-5-2][ex6-5-2]]
for river in southAmerica_rivers.values():
    print(f"- {river}")
# ex6-5-2 ends here



# #+RESULTS: ex6-5-2
# : -Paraná
# : -Beni
# : -Amazon

# <<l_code:ex6-5-3>>
# #+name: ex6-5-3

# [[file:../../Notes.org::ex6-5-3][ex6-5-3]]
for country in southAmerica_rivers.keys():
    print(f"- {country}")
# ex6-5-3 ends here

# Exercise 6-6 Polling
# Use the code in =favorite_languages.py=.
# - Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not. 
# - Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If they have not yet taken the poll, print a message inviting them to take the poll.

# [[file:../../Notes.org::*Exercise 6-6 Polling][Exercise 6-6 Polling:1]]
people = ['jen', 'sarah', 'tom', 'martha']
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

for person in people:
    if person in favorite_languages.keys():
        print(f"{person.title()}, Thank you for your cooperation")
    else:
        print(f"{person.title()}, Tell me your favorite computer language:")
# Exercise 6-6 Polling:1 ends here

# Exercise 6-7 People:
# Start with the program you wrote for Exercise 6-1. Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

# [[file:../../Notes.org::*Exercise 6-7 People:][Exercise 6-7 People::1]]
iuser1 = {"first_name": "kumi",
          "last_name": "ko",
          "age": 36,
          "city": "tokyo"}

iuser2 = {"first_name": "ian",
          "last_name": "yang",
          "age": 34,
          "city": "new orleans"}

iuser3 = {"first_name": "pedro",
          "last_name": "perez",
          "age": 36,
          "city": "bogota"}

people = [iuser1, iuser2, iuser3]
for iuser in people:
    for key, val in iuser.items():
        print(f"{key}: {val}")
    print("")
# Exercise 6-7 People::1 ends here

# Exercise 6-8 Pets
# Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called =pets=. Next, loop through your list and as you do, print everything you know about each pet.

# [[file:../../Notes.org::*Exercise 6-8 Pets][Exercise 6-8 Pets:1]]
ipet1 = {'name': 'timio',
         'type': 'hamster',
         'owner': 'tim'}

ipet2 = {'name': 'homer',
         'type': 'parrot',
         'owner': 'ale'}

ipet3 = {'name': 'sasha',
         'type': 'cat',
         'owner': 'mayra'}

pets = [ipet1, ipet2, ipet3]

for pet in pets:
    for data, value in pet.items():
        print(f"{data}: {value}")
    print("----------")
# Exercise 6-8 Pets:1 ends here

# Exercise 6-9 Favorite Places
# Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

# [[file:../../Notes.org::*Exercise 6-9 Favorite Places][Exercise 6-9 Favorite Places:1]]
favorite_places = {'juana': ['tokyo', 'san francisco'],
                   'carlos': 'gainesville',
                   'newtow': ['morogoro', 'gainesville']}

for user, places in favorite_places.items():
    print(f"{user.title()} favorite places are:")
    if type(places) is list:
        for place in places:
            print(f"- {place.title()}")
    else:
        print(f"- {places.title()}")
# Exercise 6-9 Favorite Places:1 ends here

# Exercise 6-10 Favorite Numbers
# Modify your program from Exercise 6-2,  so each person can have more than one favorite number. Then print each per- son’s name along with their favorite numbers.

# [[file:../../Notes.org::*Exercise 6-10 Favorite Numbers][Exercise 6-10 Favorite Numbers:1]]
inumbers = {"anna": 24,
            "kira": 12,
            "jane": [39, 12, 15],
            "joan": 45,
            "justine": 50}
print("Favorite numbers")
for key, val in inumbers.items():
    if isinstance(val, int):
        print(f"{key.title()}: {val}")
    else:
        print(f"{key.title()}:", end=" ")
        print(*val, sep=', ')
# Exercise 6-10 Favorite Numbers:1 ends here

# Exercise 6-11 Cities
# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the infor- mation you have stored about it.

# [[file:../../Notes.org::*Exercise 6-11 Cities][Exercise 6-11 Cities:1]]
cities_info = {
    "New York City": {
        "Average Population": 8800000,
        "Average Age": 36,
        "Main Language": "English"
    },
    "Tokyo": {
        "Average Population": 14000000,
        "Average Age": 45,
        "Main Language": "Japanese"
    },
    "Seoul": {
        "Average Population": 9700000,
        "Average Age": 42,
        "Main Language": "Korean"
    }
}

for city, info in cities_info.items():
    print(f"Information about {city}:")
    for key, data in info.items():
        print(f"{key}: {data}")
    print("")
# Exercise 6-11 Cities:1 ends here

# Exercise 6-12 Extensions
# We’re now working with examples that are complex enough that they can be extended in any number of ways. Use one of the example programs from this chapter, and extend it by adding new keys and values, chang- ing the context of the program or improving the formatting of the output.

# [[file:../../Notes.org::*Exercise 6-12 Extensions][Exercise 6-12 Extensions:1]]
for city, info in cities_info.items():
    print(f"Information about {city}:")
    for key, data in info.items():
        if isinstance(data, int):
            f_data = "{:,}".format(data)
            print(f"{key}: {f_data}")
        else:
            print(f"{key}: {data}")
    print("")
# Exercise 6-12 Extensions:1 ends here
