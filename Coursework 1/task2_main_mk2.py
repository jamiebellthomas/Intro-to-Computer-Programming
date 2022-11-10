#REDO OF Task 2 Main
from task2_functions import *
entry_talley = 0
while True:
    user_input,entry_talley = user_input_function(entry_talley)
    user_input, character_check_success = character_check(user_input)
    if character_check_success == False:
        continue
    user_input, correct_format_check_success = format_check(user_input)
    if correct_format_check_success == False:
        continue
    user_input, distinct_symbol_check_success, distinct_symbol_list = distinct_symbol_check(user_input)
    if distinct_symbol_check_success == False:
        continue
    element_symbol_check_success = element_symbol_check(distinct_symbol_list)
    if element_symbol_check_success == False:
        continue
    else:
        break
    print("Element Symbol Check Success:",element_symbol_check_success)
    print("Distinct Symbol Check Success:",distinct_symbol_check_success)
    print("Correct Format Success:",correct_format_check_success)
    print("Character Check Success:",character_check_success)
    print("User Input:",user_input)
    break