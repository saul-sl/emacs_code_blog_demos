#!/bin/python3
# Exercise 8-15 Printing Models
# Put the functions for the example =printing_models.py= in a separate file called =printing_functions.py=. Write an import statement at the top of =printing_models.py=, and modify the file to use the imported functions.

# <<l_code:printing-models>>
# #+name: code:printing-models

# [[file:../../Notes.org::code:printing-models][code:printing-models]]
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
# code:printing-models ends here
