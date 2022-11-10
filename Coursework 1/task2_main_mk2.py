#REDO OF Task 2 Main
from task2_functions import *
entry_talley = 0
while True:
    user_input,entry_talley,user_exit = user_input_function(entry_talley)
    user_input, character_check_success = character_check(user_input)
    if user_exit == True:
        break
    if character_check_success == False:
        print("Character Check Success:",character_check_success)
        continue
    user_input, correct_format_check_success = format_check(user_input)
    if correct_format_check_success == False:
        print("Correct Format Success:",correct_format_check_success)
        continue
    user_input, distinct_symbol_check_success, distinct_symbol_list = distinct_symbol_check(user_input)
    if distinct_symbol_check_success == False:
        print("Distinct Symbol Check Success:",distinct_symbol_check_success)
        continue
    element_symbol_check_success = element_symbol_check(distinct_symbol_list)
    if element_symbol_check_success == False:
        print("Element Symbol Check Success:",element_symbol_check_success)
        continue
    print("Element Symbol Check Success:",element_symbol_check_success)
    print("Distinct Symbol Check Success:",distinct_symbol_check_success)
    print("Correct Format Success:",correct_format_check_success)
    print("Character Check Success:",character_check_success)
    print("User Input:",user_input)
    break

if user_exit == True:
    print("User Input:",user_input)
    print("Entry Talley:",entry_talley)
    print("User Exit:",user_exit)
    print("Program Terminated")
else:
    print("Input Accepted!")
    print('-----------------')
    print("Chemical Forumla:",chemical_formula_builder(user_input))
    print("Atomic Mass:",atomic_mass_calculator(user_input))
    print("Attempts:",entry_talley)
    print("Thank you for using the chemical formula calculator!")
