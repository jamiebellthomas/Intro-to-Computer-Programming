#REDO OF Task 2 Main
from task2_functions import *
entry_talley = 0
# This code makes use of the check functions defined in task2_functions.py
# The check functions are called inside the while loop and return a boolean value.
# The boolean value is used to determine if that test has been passed. If
# the boolean value is True, the test has been passed. This will move the user's input into the next test 'shell'
# If a check fails, the user is returned to the first shell to try again with a new input.
# The while loop is broken when the user input has passed all tests and the user input is passed into the builder and calculator functions.
while True:
    user_input,entry_talley,user_exit = user_input_function(entry_talley)
    if user_exit == True:
        break
    user_input, character_check_success = character_check(user_input)
    if character_check_success == False:
        print("Character Check Success:",character_check_success)
        continue
    user_input, correct_format_check_success = format_check(user_input)
    if correct_format_check_success == False:
        print("Correct Format Success:",correct_format_check_success)
        continue
    distinct_symbol_check_success, distinct_symbol_list = distinct_symbol_check(user_input)
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
    print("Entry Tally:",entry_talley)
    print("User Exit:",user_exit)
    print("Program Terminated")
else:
    print("Input Accepted!")
    print('-----------------')
    print("Chemical Forumla:",chemical_formula_builder(user_input))
    print("Atomic Mass:",atomic_mass_calculator(user_input))
    print("Attempts:",entry_talley)
    print("Thank you for using the chemical formula calculator!")
