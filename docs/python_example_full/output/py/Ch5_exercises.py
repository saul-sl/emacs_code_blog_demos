#!/bin/python3
# Exercise 5-1 Conditional Tests
# Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.
# - Look closely at your results, and make sure you understand why each line evaluates to True or False. 
# - Create at least ten tests. Have at least five tests evaluate to True and another five tests evaluate to False.

#   For this exercise, a special type of print statement will be used so that the expression and its evaluation will be printed. The statement has the following form src_python[:eval no]{print(f"{<expr> = }")}. 

# [[file:../../Notes.org::*Exercise 5-1 Conditional Tests][Exercise 5-1 Conditional Tests:1]]
print("My home town is La Paz:  home_town = 'la paz'")
home_town = 'la paz'

print(f"{home_town.title() == 'La Paz' = }")
print(f"{home_town.title() == 'La paz' = }")

print("\nAverage income in Japan in yen:  jp_av_income = 6200000 ")
jp_av_income = 6200000
print(f"{jp_av_income == 6_200_000 = }")
print(f"{jp_av_income == 6200000 = }")

print(f"\nComparing numbers:")
print(f"{5 == 5.0 = }")
print(f"{5 is 5.0 = }")
# Exercise 5-1 Conditional Tests:1 ends here

# Exercise 5-2 More Conditional Tests
# You don’t have to limit the number of tests you create to ten. If you want to try more comparisons, write more tests and add them to =conditional_tests.py=. Have at least one True and one False result for each of the following: 
# - Tests for equality and inequality with strings 
# - Tests using the lower() method 
# - Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to 
# - Tests using the and keyword and the or keyword 
# - Test whether an item is in a list 
# - Test whether an item is not in a list

# [[file:../../Notes.org::*Exercise 5-2 More Conditional Tests][Exercise 5-2 More Conditional Tests:1]]
# Tests for equality and inequality with strings
print("Define two strings str1 = 'la paz' and str2 = 'La Paz'")
str1 = 'la paz'
str2 = 'La Paz'
print(f"{str1 == str2 = }")

# Tests using the lower() method
print(f"{str1 == str2.lower() = }")

# Numerical tests involving equality and inequality,
# greater than and less than, greater than or equal to,
# and less than or equal to
print("\nDefine two numbers inum1 = 25 and inum2 = 40")
inum1 = 25
inum2 = 40

print(f"{inum1 == inum2 = }")
print(f"inum1 != inum2 = {inum1 != inum2}")
print(f"{inum1+25 < inum2 = }")
print(f"{inum1 >= inum2-25 = }")

# Tests using the and keyword and the or keyword
print(f"{25 < 35 and 34 > 23 = }")
print(f"{inum1 == inum2 or inum2 > inum1 = }")

# Test whether an item is in a list
my_foods = ['pizza', 'fried chicken', 'tuna', 'chicken soup']
my_food = 'chicken'
print(f"\nFood I have: my_foods = {my_foods}")
print(f"Food I search: my_food = {my_food}")

print(f"{my_food in my_foods = }")

# Test whether an item is not in a list
print(f"{my_food not in my_foods = }")
# Exercise 5-2 More Conditional Tests:1 ends here

# Exercise 5-3 Alien Colors #1
# Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'. 
# - Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points (line [[(first-v)]]). 
# - Write one version of this program that passes the if test and another that fails. (The version that fails will have no output, line [[(second-v)]])

# [[file:../../Notes.org::*Exercise 5-3 Alien Colors #1][Exercise 5-3 Alien Colors #1:1]]
print("This is the first version of the test:")
alien_color = 'green'

if alien_color == 'green':
    print('You have earned 5pts')

print("This is the second version of the test:")
alien_color = 'blue'

if alien_color == 'green':
    print('You have earned 5pts')
# Exercise 5-3 Alien Colors #1:1 ends here

# Exercise 5-4 Alien Colors #2
# Choose a color for an alien as you did in Exercise 5-3, and write an if- else chain. 
# - If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien. 
# - If the alien’s color isn’t green, print a statement that the player just earned 10 points. 
# - Write one version of this program that runs the if block and another that runs the else block.

# For this exercise Org's header argument, =:var= is used to define the color of the alien, by default =green=. Then, for the second version of the code, the a code block is written using the header argument =:noweb yes= so, that the code from the first block can be inserted. Additionally, the color variable is set to =blue= so that the =else:= block is run. Finally, to avoid, printing the code again, the header argument =:exports results= is used.

# #+name: code:ex5-4

# [[file:../../Notes.org::code:ex5-4][code:ex5-4]]
icolor="green"
print(f"The value of icolor is: {icolor}")

if alien_color == icolor:
    print('You have earned 5pts')
else:
    print("You have earned 10pts")
# code:ex5-4 ends here



# #+RESULTS: code:ex5-4
# : You have earned 5pts


# [[file:../../Notes.org::*Exercise 5-4 Alien Colors #2][Exercise 5-4 Alien Colors #2:2]]
icolor="blue"
print(f"The value of icolor is: {icolor}")

if alien_color == icolor:
    print('You have earned 5pts')
else:
    print("You have earned 10pts")
# Exercise 5-4 Alien Colors #2:2 ends here

# Exercise 5-5 Alien Colors #3
# Turn your if- else chain from Exercise 5-4 into an if- elif- else chain. 
# - If the alien is green, print a message that the player earned 5 points. 
# - If the alien is yellow, print a message that the player earned 10 points. 
# - If the alien is red, print a message that the player earned 15 points. 
# - Write three versions of this program, making sure each message is printed for the appropriate color alien.

# #+name: code:ex5-5  

# [[file:../../Notes.org::code:ex5-5][code:ex5-5]]
icolor="green"
print(f"The value of icolor is: {icolor}")

if alien_color == 'green':
    print('You have earned 5pts')
elif alien_color == 'red':
    print("You have earned 15pts")
elif alien_color == 'yellow':
    print("You have earned 10pts")
# code:ex5-5 ends here

# [[file:../../Notes.org::*Exercise 5-5 Alien Colors #3][Exercise 5-5 Alien Colors #3:2]]
icolor="red"
print(f"The value of icolor is: {icolor}")

if alien_color == icolor:
    print('You have earned 5pts')
else:
    print("You have earned 10pts")
# Exercise 5-5 Alien Colors #3:2 ends here

# [[file:../../Notes.org::*Exercise 5-5 Alien Colors #3][Exercise 5-5 Alien Colors #3:3]]
icolor="yellow"
print(f"The value of icolor is: {icolor}")

if alien_color == icolor:
    print('You have earned 5pts')
else:
    print("You have earned 10pts")
# Exercise 5-5 Alien Colors #3:3 ends here

# Exercise 5-6 Stages of Life
# Write an if- elif- else chain that determines a person’s stage of life. Set a value for the variable age, and then: 
# - If the person is less than 2 years old, print a message that the person is a baby. 
# - If the person is at least 2 years old but less than 4, print a message that the person is a toddler. 
# - If the person is at least 4 years old but less than 13, print a message that the person is a kid. 
# - If the person is at least 13 years old but less than 20, print a message that the person is a teenager. 
# - If the person is at least 20 years old but less than 65, print a message that the person is an adult. 
# - If the person is age 65 or older, print a message that the person is an elder.

# #+name: code:ex5-6

# [[file:../../Notes.org::code:ex5-6][code:ex5-6]]
age=40
print(f"Your age is {age}.")
imessage = "You are classified as,"
if iage < 2:
    print(imessage, "baby")
elif iage <4 and iage >= 2:
    print(imessage, "toddler")
elif iage <13 and iage >= 4:
    print(imessage, "kid")
elif iage <20 and iage >= 13:
    print(imessage, "teenager")
elif iage <65 and iage >= 20:
    print(imessage, "adult")
elif iage >= 65:
    print(imessage, "elder")
# code:ex5-6 ends here

# Exercise 5-7 Favorite Fruit
# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list. 
# - Make a list of your three favorite fruits and call it favorite_fruits. 
# - Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

# #+name: code:ex5-7

# [[file:../../Notes.org::code:ex5-7][code:ex5-7]]
my_fruit="kiwi"
my_fruits = ['kiwi', 'apple', 'banana']

print(f"You are searching for {my_fruit}")
if my_fruit in my_fruits:
    print(f"You really like, {my_fruit.title()}")
else:
    print(f"It is good to try new fruits")
# code:ex5-7 ends here

# [[file:../../Notes.org::*Exercise 5-7 Favorite Fruit][Exercise 5-7 Favorite Fruit:2]]
my_fruit="mango"
my_fruits = ['kiwi', 'apple', 'banana']

print(f"You are searching for {my_fruit}")
if my_fruit in my_fruits:
    print(f"You really like, {my_fruit.title()}")
else:
    print(f"It is good to try new fruits")
# Exercise 5-7 Favorite Fruit:2 ends here



# #+RESULTS:
# : You are searching for mango
# : It is good to try new fruits


# [[file:../../Notes.org::*Exercise 5-7 Favorite Fruit][Exercise 5-7 Favorite Fruit:3]]
my_fruit="apple"
my_fruits = ['kiwi', 'apple', 'banana']

print(f"You are searching for {my_fruit}")
if my_fruit in my_fruits:
    print(f"You really like, {my_fruit.title()}")
else:
    print(f"It is good to try new fruits")
# Exercise 5-7 Favorite Fruit:3 ends here

# [[file:../../Notes.org::*Exercise 5-7 Favorite Fruit][Exercise 5-7 Favorite Fruit:4]]
my_fruit="banana"
my_fruits = ['kiwi', 'apple', 'banana']

print(f"You are searching for {my_fruit}")
if my_fruit in my_fruits:
    print(f"You really like, {my_fruit.title()}")
else:
    print(f"It is good to try new fruits")
# Exercise 5-7 Favorite Fruit:4 ends here

# [[file:../../Notes.org::*Exercise 5-7 Favorite Fruit][Exercise 5-7 Favorite Fruit:5]]
my_fruit="orange"
my_fruits = ['kiwi', 'apple', 'banana']

print(f"You are searching for {my_fruit}")
if my_fruit in my_fruits:
    print(f"You really like, {my_fruit.title()}")
else:
    print(f"It is good to try new fruits")
# Exercise 5-7 Favorite Fruit:5 ends here

# Exercise 5-8 Hello Admin
# Make a list of five or more usernames, including the name 'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
# - If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report? 
# - Otherwise, print a generic greeting, such as "/Hello Jaden, thank you for logging in again/".

# [[file:../../Notes.org::*Exercise 5-8 Hello Admin][Exercise 5-8 Hello Admin:1]]
users = ['tom', 'anna', 'mark', 'admin', 'steve', 'emma']

for user in users:
    if user in users:
        if user == 'admin':
            print("* Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, welcome!")
# Exercise 5-8 Hello Admin:1 ends here

# Exercise 5-9 No Users
# Add an if test to =hello_admin.py= to make sure the list of users is not empty.
# - If the list is empty, print the message "/We need to find some users!/" 
# - Remove all of the usernames from your list, and make sure the correct message is printed.

# [[file:../../Notes.org::*Exercise 5-9 No Users][Exercise 5-9 No Users:1]]
users = []
if users:
    if user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, welcome!")
else:
    print("We need to find some users!")
# Exercise 5-9 No Users:1 ends here

# Exercise 5-10 Checking Usernames
# Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# - Make a list of five or more usernames called current_users. 
# - Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list. 
# - Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available. 
# - Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)
  

# [[file:../../Notes.org::*Exercise 5-10 Checking Usernames][Exercise 5-10 Checking Usernames:1]]
current_users = ['tim', 'tom', 'Mike', 'saul', 'anna', 'admin']
new_users = ['jane', 'mikah', 'liah', 'Tom', 'mike']
current_users_test = [user.lower() for user in current_users]

for user in new_users:
    print(f"- Trying to log as {user}...")
    usert = user.lower()
    if usert in current_users_test:
        print(f"  The name, {user} is already taken")
        print(f'   Note that usernames are case-insensitive')
    else:
        print(f"  The name, {user} is available")
    print("")
# Exercise 5-10 Checking Usernames:1 ends here

# Exercise 5-11 Ordinal Numbers
# Ordinal numbers indicate their position in a list, such as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# - Store the numbers 1 through 9 in a list. 
# - Loop through the list. 
# - Use an if- elif- else chain inside the loop to print the proper ordinal end- ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line.

# [[file:../../Notes.org::*Exercise 5-11 Ordinal Numbers][Exercise 5-11 Ordinal Numbers:1]]
inumbers = list(range(1, 10))
for i in inumbers:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
# Exercise 5-11 Ordinal Numbers:1 ends here
