#!/bin/python3


# #+RESULTS: code:printing-models


# [[file:../../Notes.org::*Exercise 8-15 Printing Models][Exercise 8-15 Printing Models:2]]
import sys
sys.path.append("output/py")  
from printing_functions import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
# Exercise 8-15 Printing Models:2 ends here

# Exercise 8-16 Imports
# Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches
# 1) =import module_name= ([[l_code:Ch8ex16-1][\rightarrow]])
# 2) =from module_name import function_name= ([[l_code:Ch8ex16-2][\rightarrow]])
# 3) =from module_name import function_name as fn= ([[l_code:Ch8ex16-3][\rightarrow]])
# 4) =import module_name as mn= ([[l_code:Ch8ex16-4][\rightarrow]])
# 5) =from module_name import *= ([[l_code:Ch8ex16-5][\rightarrow]])

#    The module that will be imported is =list_processing.py= where a function that splits a list into two subsets is defined (=split_list=). To import the function as indicated above a list to work on is created first. Then we import and use the function as indicated in the caption.
  
# <<l_code:create-list>>
# #+name: code:create-list

# [[file:../../Notes.org::code:create-list][code:create-list]]
African_countries_sample = ['Libya', 'Morocco', 'Sudan', 'Togo',
                            'Gabon', 'Zambia', 'Uganda', 'Tunisia',
                            'Ethiopia', 'Burundi', 'Benin', 'Egypt',
                            'Central African Republic', 'Namibia',
                            'Gambia', 'Djibouti', 'Mauritania',
                            'Tanzania', 'Eritrea', 'Malawi']
# code:create-list ends here



# <<l_code:Ch8ex16-1>>
# #+name: code:Ch8ex16-1
# #+caption: Exercise 16 part 1, =import module_name=  

# [[file:../../Notes.org::code:Ch8ex16-1][code:Ch8ex16-1]]
import list_processing

Subset_1, Subset_2 = [], []

list_processing.split_list(African_countries_sample,Subset_1, Subset_2)
list_processing.print_items(Subset_1)
# code:Ch8ex16-1 ends here



# #+RESULTS: code:Ch8ex16-1
# #+begin_example
# - Libya
# - Sudan
# - Gabon
# - Uganda
# - Ethiopia
# - Benin
# - Central African Republic
# - Gambia
# - Mauritania
# - Eritrea
# #+end_example

# <<l_code:Ch8ex16-2>>
# #+name: code:Ch8ex16-2
# #+caption: Exercise 16 part 2, =from module_name import function_name=  

# [[file:../../Notes.org::code:Ch8ex16-2][code:Ch8ex16-2]]
from list_processing import split_list

Subset_1, Subset_2 = [], []

split_list(African_countries_sample,Subset_1, Subset_2)
for country in Subset_1:
    print(f"- {country}")
# code:Ch8ex16-2 ends here



# <<l_code:Ch8ex16-3>>
# #+name: code:Ch8ex16-3
# #+caption: Exercise 16 part 3, =from module_name import function_name as fn=  

# [[file:../../Notes.org::code:Ch8ex16-3][code:Ch8ex16-3]]
from list_processing import split_list as spl

Subset_1, Subset_2 = [], []

spl(African_countries_sample,Subset_1, Subset_2)
for country in Subset_1:
    print(f"- {country}")
# code:Ch8ex16-3 ends here



# <<l_code:Ch8ex16-4>>
# #+name: code:Ch8ex16-4
# #+caption: Exercise 16 part 4, =import module_name as mn= 

# [[file:../../Notes.org::code:Ch8ex16-4][code:Ch8ex16-4]]
import list_processing as listp

Subset_1, Subset_2 = [], []

listp.split_list(African_countries_sample,Subset_1, Subset_2)
listp.print_items(Subset_1)
# code:Ch8ex16-4 ends here



# <<l_code:Ch8ex16-5>>
# #+name: code:Ch8ex16-5
# #+caption: Exercise 16 part 5, =from module_name import *=   

# [[file:../../Notes.org::code:Ch8ex16-5][code:Ch8ex16-5]]
from list_processing import * 

Subset_1, Subset_2 = [], []

split_list(African_countries_sample,Subset_1, Subset_2)
print_items(Subset_1)
# code:Ch8ex16-5 ends here
