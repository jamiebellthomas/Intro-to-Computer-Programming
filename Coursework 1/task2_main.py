#Task 2 mk2
from task2_functions import *
entry_talley = 0
character_check_success = False
correct_format_check_success = False
distinct_symbol_check_success = False
element_symbol_check_success = False
"""
Each 'check' function returns a boolean 'check success' value. The boolean value is used to determine if that test has been passed. If
the boolean value is True, the test has been passed. This will break the while loop that check is in and move the user's input into the next test 'shell'
If a check fails, all previous checks are reset to false and the user is returned to the first shell to try again with a new input.
"""
while element_symbol_check_success == False:
    while distinct_symbol_check_success == False:
        while correct_format_check_success == False:
            while character_check_success == False:
                user_input,entry_talley = user_input_function(entry_talley)
                # 1) The first step of the inner most loop is to collect the user input.
                user_input, character_check_success = character_check(user_input)
                # 2) The second step is to check the user input for illegal characters. 
                # If the user input contains illegal characters character_check_success will be set to False and 
                # the first loop will recur until the user enters a valid input. 
                print("Character Check Success:",character_check_success)
                # This informs the user the character check status

            user_input, correct_format_check_success = format_check(user_input)
            # 3) The third step is to check the user input for the correct format.
            print("Correct Format Success:",correct_format_check_success)
            # This informs the user the format check status
            if correct_format_check_success == False:
                character_check_success = False
                # If the user input is not in the correct format, the character check is reset to False and the user is returned to the first loop enter a new input.     
                # If the correct format test is passed, the correct_format_check_success = True, the format test loop is broken and
                # the user input is moved to the next test 'shell'    

        user_input, distinct_symbol_check_success, distinct_symbol_list = distinct_symbol_check(user_input)
        # 4) The fourth step is to check the user input for distinct symbols.
        print("Distinct Symbol Check Success:",distinct_symbol_check_success)
        # This informs the user the distinct symbol check status
        if distinct_symbol_check_success == False:
            correct_format_check_success = False
            character_check_success = False 
            # If the user input does not contain distinct symbols, the character check and correct format checks are reset 
            # to False and the user is returned to the first loop to enter a new input.
            # If the distinct symbol test is passed, the distinct_symbol_check_success = True, the distinct symbol test 
            # loop is broken and he user input is moved to the next test 'shell'

    element_symbol_check_success = element_symbol_check(distinct_symbol_list)
    # 5) The fifth step is to check the user input for valid element symbols.
    print("Element Symbol Check Success:",element_symbol_check_success)
    # This informs the user the element symbol check status

    if element_symbol_check_success == False:
        distinct_symbol_check_success = False
        correct_format_check_success = False
        character_check_success = False
        # If the user input does not contain valid element symbols, the character check, correct format and distinct symbol checks 
        # are reset to False and the user is returned to the first loop to enter a new input.
        # If the element symbol test is passed, the element_symbol_check_success = True, the element symbol test loop is broken and
        # the user input has passed all tests and is printed to the screen and the user input is passed into the builder and calculator functions.



print("Input Accepted!")
print('-----------------')
print("User inputs:",user_input)
print("Chemical Forumla:",chemical_formula_builder(user_input))
print("Atomic Mass:",atomic_mass_calculator(user_input))
print("Attempts:",entry_talley)
print("Thank you for using the chemical formula calculator!")

