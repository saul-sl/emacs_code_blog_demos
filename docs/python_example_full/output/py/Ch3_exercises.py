#!/bin/python3
# Exercise 3-1 Names
# Store the names of a few of your friends in a list called =names=. Print each person’s name by accessing each element in the list, one at a time.

# [[file:../../Notes.org::*Exercise 3-1 Names][Exercise 3-1 Names:1]]
names = ['tim', 'tom', 'sam']

print(names[0].title())
print(names[1].title())
print(names[2].title())
# Exercise 3-1 Names:1 ends here

# Exercise 3-2 Greetings
# Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

# [[file:../../Notes.org::*Exercise 3-2 Greetings][Exercise 3-2 Greetings:1]]
print(f"Hello {names[0].title()}, welcome back!")
print(f"Hello {names[1].title()}, welcome back!")
print(f"Hello {names[2].title()}, welcome back!")
# Exercise 3-2 Greetings:1 ends here

# Exercise 3-3 Your Own List
# Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as /"I would like to own a Honda motorcycle."/

# [[file:../../Notes.org::*Exercise 3-3 Your Own List][Exercise 3-3 Your Own List:1]]
transportation_modes = ['bicycle', 'train', 'bus']
print(f"I rarely move by {transportation_modes[0]}")
print(f"I used to ride the {transportation_modes[1]} a lot")
print(f"Nowadays I mainly use the {transportation_modes[2]}")
# Exercise 3-3 Your Own List:1 ends here

# Exercise 3-4 Guest list
# If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

# [[file:../../Notes.org::*Exercise 3-4 Guest list][Exercise 3-4 Guest list:1]]
guests = ['linus', 'tim', 'tom']
msg_end = "I would like to invite you to have dinner"

print(f"Dear {guests[0].title()}, {msg_end}")
print(f"Dear {guests[1].title()}, {msg_end}")
print(f"Dear {guests[2].title()}, {msg_end}")
# Exercise 3-4 Guest list:1 ends here

# Exercise 3-5 Changing Guest List
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# - Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# - Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# - Print a second set of invitation messages, one for each person who is still in your list.

# [[file:../../Notes.org::*Exercise 3-5 Changing Guest List][Exercise 3-5 Changing Guest List:1]]
for guest in guests:
    print(f"Dear {guest.title()}, {msg_end}")

print(f"\nUnfortunatelly, {guests[0].title()} won't come for dinner\n")

guests.remove('linus')
guests.append('steve')

print(f"Dear {guests[len(guests)-1].title()}, {msg_end}")
# Exercise 3-5 Changing Guest List:1 ends here

# Exercise 3-6 More Guests
# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# - Start with your program from Exercise 3-4 or Exercise 3-5. Add a =print()= call to the end of your program informing people that you found a bigger dinner table.
# - Use =insert()= to add one new guest to the beginning of your list.
# - Use =insert()= to add one new guest to the middle of your list.
# - Use =append()= to add one new guest to the end of your list.
# - Print a new set of invitation messages, one for each person in your list.


# [[file:../../Notes.org::*Exercise 3-6 More Guests][Exercise 3-6 More Guests:1]]
for guest in guests:
    print(f"- Dear {guest.title()}, {msg_end}")

print(f"\nWe found a bigger place to host the dinner\n")

# Append new guests to the list
guests.insert(0, "tina")
guests.insert(2, "anna")
guests.insert(len(guests), "maya")

for guest in guests:
    print(f"- Dear {guest.title()}, {msg_end}")
# Exercise 3-6 More Guests:1 ends here

# Exercise 3-7  Shrinking Guest List
# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

# - Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.

# [[file:../../Notes.org::*Exercise 3-7 Shrinking Guest List][Exercise 3-7  Shrinking Guest List:1]]
print("Change of plans, now only two people can come to dinner\n")
# Exercise 3-7  Shrinking Guest List:1 ends here


  
# - Use =pop()= to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.

# [[file:../../Notes.org::*Exercise 3-7 Shrinking Guest List][Exercise 3-7  Shrinking Guest List:2]]
while len(guests) > 2:
    out_guest = guests.pop()
    print(f"- Sorry, {out_guest.title()} we can't have you for dinner.")
# Exercise 3-7  Shrinking Guest List:2 ends here


  
# - Print a message to each of the two people still on your list, letting them know they’re still invited.

# [[file:../../Notes.org::*Exercise 3-7 Shrinking Guest List][Exercise 3-7  Shrinking Guest List:3]]
for guest in guests:
    print(f"- Dear {guest.title()}, please come to dinner")
# Exercise 3-7  Shrinking Guest List:3 ends here


  
# - Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

# [[file:../../Notes.org::*Exercise 3-7 Shrinking Guest List][Exercise 3-7  Shrinking Guest List:4]]
while guests:
    del guests[0]

print(guests)
# Exercise 3-7  Shrinking Guest List:4 ends here

# Exercise 3-8 Seeing the World
# Think of at least five places in the world you’d like to visit.

# - Store the locations in a list. Make sure the list is not in alphabetical order.  Then, print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list ([[l_code:Ch3ex8-1][\rightarrow]]).
# - Use =sorted()= to print your list in alphabetical order without modifying the actual list ([[l_code:Ch3ex8-2l][\rightarrow]]).
# - Show that your list is still in its original order by printing it  ([[l_code:Ch3ex8-3][\rightarrow]]).
# - Use =sorted()= to print your list in reverse alphabetical order without changing the order of the original list ([[l_code:Ch3ex8-4][\rightarrow]]).
# - Show that your list is still in its original order by printing it again ([[l_code:Ch3ex8-3rep][\rightarrow]]). 
# - Use =reverse()= to change the order of your list. Print the list to show that its order has changed ([[l_code:Ch3ex8-5][\rightarrow]]). 
# - Use =reverse()= to change the order of your list again. Print the list to show it’s back to its original order ([[l_code:Ch3ex8-6][\rightarrow]]). 
# - Use =sort()= to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed ([[l_code:Ch3ex8-7][\rightarrow]]). 
# - Use =sort()= to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed  ([[l_code:Ch3ex8-8][\rightarrow]]).

# <<l_code:Ch3ex8-1>>
# #+name: code:Ch3ex8-1
# #+caption: Exercise 8 part 1

# [[file:../../Notes.org::code:Ch3ex8-1][code:Ch3ex8-1]]
itravel = ['thailand', 'colombia', 'chile',
           'tanzania', 'madagascar']

print("Unsorted list")
for place in itravel:
    print(f"- {place.title()}")
# code:Ch3ex8-1 ends here




# <<l_code:Ch3ex8-2>>
# #+name: code:Ch3ex8-2
# #+label: code:Ch3ex8-2l
# #+caption: Exercise 8 part 2

# [[file:../../Notes.org::code:Ch3ex8-2l][code:Ch3ex8-2l]]
print("Sorted list")
for place in sorted(itravel):
    print(f"- {place.title()}")
# code:Ch3ex8-2l ends here




# <<l_code:Ch3ex8-3>>
# #+name: code:Ch3ex8-3
# #+caption: Exercise 8 part 3

# [[file:../../Notes.org::code:Ch3ex8-3][code:Ch3ex8-3]]
print("Check that list is in the same order")
for place in itravel:
    print(f"- {place.title()}")
# code:Ch3ex8-3 ends here



# <<l_code:Ch3ex8-4>>
# #+name: code:Ch3ex8-4
# #+caption: Exercise 8 part 4

# [[file:../../Notes.org::code:Ch3ex8-4][code:Ch3ex8-4]]
print("Sorted list in reverse order")
for place in sorted(itravel, reverse=True):
    print(f"- {place.title()}")
# code:Ch3ex8-4 ends here



# <<Ch3ex8-3rep>>
# Re-evaluate the code from [[l_code:Ch3ex8-3][part 3]].
# ##+call: code:Ch3ex8-3()

# <<l_code:Ch3ex8-5>>
# #+name: code:Ch3ex8-5
# #+caption: Exercise 8 part 5

# [[file:../../Notes.org::code:Ch3ex8-5][code:Ch3ex8-5]]
# Reverse list
print("Reverse list")
itravel.reverse()
for place in itravel:
    print(f"- {place.title()}")
# code:Ch3ex8-5 ends here



# <<l_code:Ch3ex8-6>>
# #+name: code:Ch3ex8-6
# #+caption: Exercise 8 part 6

# [[file:../../Notes.org::code:Ch3ex8-6][code:Ch3ex8-6]]
# Re-reverse list
print("Reverse list (again)")
itravel.reverse()
for place in itravel:
    print(f"- {place.title()}")
# code:Ch3ex8-6 ends here



# <<l_code:Ch3ex8-7>>
# #+name: code:Ch3ex8-7
# #+caption: Exercise 8 part 7

# [[file:../../Notes.org::code:Ch3ex8-7][code:Ch3ex8-7]]
# Sort list
print("Sort the list")
itravel.sort()
for place in itravel:
    print(f"- {place.title()}")
# code:Ch3ex8-7 ends here



# <<l_code:Ch3ex8-8>>
# #+name: code:Ch3ex8-8
# #+caption: Exercise 8 part 8

# [[file:../../Notes.org::code:Ch3ex8-8][code:Ch3ex8-8]]
# Sort in reverse order
print("Sort in reverse order")
itravel.sort(reverse=True)
for place in itravel:
    print(f"- {place.title()}")
# code:Ch3ex8-8 ends here

# Exercise 3-9 Dinner Guests
# Working with one of the programs from Exercises 3-4 through 3-7, use =len()= to print a message indicating the number of people you are inviting to dinner.

# [[file:../../Notes.org::*Exercise 3-9 Dinner Guests][Exercise 3-9 Dinner Guests:1]]
# guests = ['linus', 'tim', 'tom']
print(f"There will be {len(guests)} people at the dinner")
# Exercise 3-9 Dinner Guests:1 ends here

# Exercise 3-10 Every Function
# Think of something you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or any- thing else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.


# [[file:../../Notes.org::*Exercise 3-10 Every Function][Exercise 3-10 Every Function:1]]
languages = ['spanish', 'chinese', 'english', 'korean', 'swahili']

# length of a list
print(f"The list has {len(languages)} elements")

# index an element
print(f"The first item is: {languages[0].title()}")

# replace an element using an index
languages[0] = 'quechua'
print(f"\nNow the first element is: {languages[0].title()}")

# append an element 
languages.append('aymara')

# insert an element at a specific position
languages.insert(3, 'guarani')
print(f"\nNow the fourth element is: {languages[3].title()}")
print(f"And the last is: {languages[-1].title()}")

# Removing elements
print(f"\n{languages}")
print("I will now remove the 4th, the 1st and last elements")
del languages[3]
languages.pop()
languages.pop(0)
print(languages)

# sort the elements
print(sorted(languages))
languages.sort(reverse=True)
print(languages)
# Exercise 3-10 Every Function:1 ends here

# 3-11. Intentional Error
# If you haven’t received an index error in one of your programs yet, try to make one happen. Change an index in one of your programs to produce an index error. Make sure you correct the error before closing the program.

# The snippet [[l_code:index-error][below]] tries to retrieve the last item of a list using the value of the list length which will cause an error. To print it by evaluating the code a =try= block is used. Below the results the message that appears in an interactive session is presented.

# <<l_code:index-error>>
# #+name: code:index-error

# [[file:../../Notes.org::code:index-error][code:index-error]]
len_brands = len(running_shoes)
print(f"We have listed {len_brands} running shoe brands")
try:
    print(f"Brand {len_brands} is {running_shoes[len_brands]}")
except Exception as e:
    print(e)
# code:index-error ends here



# #+RESULTS: index-error
# : We have listed 6 running shoe brands
# : list index out of range


# [[file:../../Notes.org::*3-11. Intentional Error][3-11. Intentional Error:2]]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
# 3-11. Intentional Error:2 ends here
