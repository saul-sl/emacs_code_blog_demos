#!/bin/python3
# Exercise 7-1 Rental Car
# Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

# [[file:../../Notes.org::*Exercise 7-1 Rental Car][Exercise 7-1 Rental Car:1]]
message = 'What type of car do you want?\n'
user_car = input(message)
print(f"Let's see if we have a {user_car.title()} available")
# Exercise 7-1 Rental Car:1 ends here

# Exercise 7-2 Restaurant Seating
# Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message say- ing they’ll have to wait for a table. Otherwise, report that their table is ready.

# [[file:../../Notes.org::*Exercise 7-2 Restaurant Seating][Exercise 7-2 Restaurant Seating:1]]
message = "How many people are dinning?\n"
customers = input(message)
i_customers = int(customers)
  if isinstance(i_customers, int):
      if i_customers < 8:
          print("Please come this way")
      else:
          print("I'm sorry, you will have to wait for a table")
# Exercise 7-2 Restaurant Seating:1 ends here

# Exercise 7-3 Multiples of Ten
# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

# [[file:../../Notes.org::*Exercise 7-3 Multiples of Ten][Exercise 7-3 Multiples of Ten:1]]
message = "Enter a number:\n"
inum = input(message)
inum = int(inum)
inum2 = 10
if inum % inum2 == 0:
    print(f"{inum} is a multiple of {inum2}")
# Exercise 7-3 Multiples of Ten:1 ends here

# Exercise 7-4 Pizza Toppings
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

# [[file:../../Notes.org::*Exercise 7-4 Pizza Toppings][Exercise 7-4 Pizza Toppings:1]]
print("Write the pizza topping you want:")
print("Type 'quit' to exit")
toppings = []
while True:
    topping = input("Topping: ")
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza")
# Exercise 7-4 Pizza Toppings:1 ends here

# Exercise 7-5 Movie Tickets
# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

# [[file:../../Notes.org::*Exercise 7-5 Movie Tickets][Exercise 7-5 Movie Tickets:1]]
iage = input("Enter your age: ")
iage = int(iage)
if iage < 3:
    print("Ticket is free")
elif iage <= 12 and iage >= 3:
    print("Ticket costs 10$")
elif iage > 12:
    print("Ticket costs 15$")
# Exercise 7-5 Movie Tickets:1 ends here

# Exercise 7-6 Three Exits
# Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
# - Use a conditional test in the while statement to stop the loop. 
# - Use an active variable to control how long the loop runs. 
# - Use a break statement to exit the loop when the user enters a 'quit' value.

# [[file:../../Notes.org::*Exercise 7-6 Three Exits][Exercise 7-6 Three Exits:1]]
print("Enter your age: ")
print("Type 'q' to exit")
status = 'active'
  while status == 'active':
      # while True:
      iage = input("Age: ")
      try:
          iage = int(iage)
      except ValueError:
          status = 'inactive'
      else:
          if iage < 3:
              print("Ticket is free")
          elif iage <= 12 and iage >= 3:
              print("Ticket costs 10$")
          elif iage > 12:
              print("Ticket costs 15$")
# Exercise 7-6 Three Exits:1 ends here

# Exercise 7-8 Deli
# Make a list called sandwich_orders and fill it with the names of vari- ous sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

# [[file:../../Notes.org::*Exercise 7-8 Deli][Exercise 7-8 Deli:1]]
sandwich_orders = ['egg', 'tuna', 'chicken', 'beef']
finished_orders = []
while sandwich_orders:
    order = sandwich_orders.pop()
    finished_orders.append(order)
    print(f"Making a {order.title()} sandwich")

print("These sandwiches were made")
for sandwich in finished_orders:
    print(f"- {sandwich.title()}")
# Exercise 7-8 Deli:1 ends here

# Exercise 7-9 No Pastrami
# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

# [[file:../../Notes.org::*Exercise 7-9 No Pastrami][Exercise 7-9 No Pastrami:1]]
miss = 'pastrami'
sandwich_orders = ['egg', miss, 'tuna', miss, 'chicken', 'beef', miss]
finished_orders = []
print(f"We are out of {miss.title()} sandwich")
while miss in sandwich_orders:
    sandwich_orders.remove(miss)

while sandwich_orders:
    order = sandwich_orders.pop()
    finished_orders.append(order)
    print(f"Making a {order.title()} sandwich")

print("These sandwiches were made")
for sandwich in finished_orders:
    print(f"- {sandwich.title()}")
# Exercise 7-9 No Pastrami:1 ends here

# Exercise 7-10 Dream Vacation
# Write a program that polls users about their dream vaca- tion. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.

# [[file:../../Notes.org::*Exercise 7-10 Dream Vacation][Exercise 7-10 Dream Vacation:1]]
poll_results = []
message = "If you could visit one place in the world, where would you go?"
print(message)
print("Type 'q' to exit")
  while True:
      answer = input("Answer: ")
      if answer == "q":
          break
      else:
          poll_results.append(answer)

  if poll_results:
      print("These are the answers:")
      for item in poll_results:
          print(f"- {item}")
# Exercise 7-10 Dream Vacation:1 ends here
