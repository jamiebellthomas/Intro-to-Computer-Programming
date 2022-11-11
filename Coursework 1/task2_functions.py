#Task 2

def user_input_function(entry_talley):
    """
    This function takes user input and checks that:
    a) the input is not empty
    b) there are no negative symbols (all stiochiometric coefficients are positive)
    this function also also handles the attempt counter.
    """
    user_exit = False # This variable is used to check if the user has entered the exit command. At the end of the function it is returned.
    entry_talley+=1
    if entry_talley == 1:
        print("Please enter the elements you'd like to combine and their ratios (e.g 2H + 1O --> H2O)")
        print("Please enter the elements in the format: coefficient-element (e.g 2H or 1O)")
        print("Available elements are: H,He,Li,Be,B,C,N,O,F,Ne. This program is not case sensitive.")
        print("Type 'exit' to exit the program.")
        user_input = input("(Attempt 1) --> ")
        # The initial input message is different to the subsequent input messages. It contains more detail about the format of the input.
    else:
        print("Please enter the elements you'd like to combine and their ratios:")
        print("Type 'exit' to exit the program.")
        user_input = input(f"(Attempt {entry_talley}) --> ")
        # The subsequent input messages are less detailed and simply ask for the input.
    if user_input.strip().lower() == "exit":
        user_exit = True
        # If the user enters "exit" the program will exit.

    while user_input.strip() == '':
        entry_talley+=1
        print("No input detected. Please try again.")
        print("Please enter the elements you'd like to combine and their ratios:")
        print("Type 'exit' to exit the program.")
        user_input = input(f"(Attempt {entry_talley}) --> ")
        # This while loop checks that the user has entered something. If they have not, it asks them to try again and increments the attempt counter.

    while '-' in user_input:
        entry_talley+=1
        print("Negative numbers are not accepted. Please try again.")
        print("Please enter the elements you'd like to combine and their ratios:")
        print("Type 'exit' to exit the program.")
        user_input = input(f"(Attempt {entry_talley}) --> ")
        # This while loop checks that the user has not entered a negative number. If they have, it asks them to try again and increments the attempt counter.
    
    while user_input.strip() == '+':
        entry_talley+=1
        print("No elements detected. Please try again.")
        print("Please enter the elements you'd like to combine and their ratios:")
        print("Type 'exit' to exit the program.")
        user_input = input(f"(Attempt {entry_talley}) --> ")
        # This while loop checks that the user has not entered a '+' on its own. If they have, it asks them to try again and increments the attempt counter.
        # This was check was hard coded into the first check to prevent the program from crashing  during later checks when the user enters a '+' on its own.

    return user_input,entry_talley,user_exit
    
def character_check(user_input):
    """
    This function checks the user input for invalid characters by stripping the input of all valid characters and checking if the string is empty
    Once we have verified there are no illegal characters in the user input, we split the string on the +'s and strip all spaces
    """
    character_check_success = False # This variable is used to check if the character check was successful. At the end of the function it is returned.
    user_input_test = user_input.replace(" ","") # A copy of the user input (with all spaces removed) is made so that the original input is not altered.
    plus_index_record = [] # This list is used to record the index of the '+' characters in the user input.
    error_detection = 0 # This variable is used to check if any errors have been detected. If it is 0 at the end of the function, the character check was successful.
    for index,value in enumerate(user_input_test):
        if value == '+':
            plus_index_record.append(index)
            # This for loop records the index of the '+' characters in the user input.
        if value.isalpha() or value.isnumeric() or value == '+':
            user_input_test = user_input_test.translate({ord(value): None})
            # This for loop removes all valid characters from the user input copy.

    if len(plus_index_record) > 1:
        for x in range(1,len(plus_index_record)):
            if plus_index_record[x] - plus_index_record[x-1] == 1:
                print("Double '+' detected. Please try again.")
                error_detection += 1
                # This for loop checks that there are no double +'s in the user input by comparing the +'s indicies. If there are, it prints an error message and increments the error detection variable.

    if len(user_input_test) != 0:
        # If the user input copy is not empty, it means that there are invalid characters in the user input.
        illegal_characters = []
        for i in user_input_test:
            if i not in illegal_characters:
                illegal_characters.append(i)
                # This for loop adds all new illegal characters to a list.
        print(f"Illegal characters detected ({illegal_characters}). Please try again.")
        error_detection += 1
        # Once the loops are completed, the illegal characters are displayed and the error detection variable is incremented.
    if error_detection == 0:
        character_check_success = True
        user_input = (user_input.split("+"))
        for i,x in enumerate(user_input):
            user_input[i] = x.strip()
        # If the error detection variable is 0 at this stage, no errors were detected. The character check was successful and the check_success variable is set to True.
        # The user input is split on the +'s and stripped of all spaces to be sent to the next check function.
        # At this stage, an ideal user input is a list of strings, each string being a coefficient-element pair.
    return user_input,character_check_success
    
def format_check(user_input):
    """
    Once we have verified there are no illegal characters in the user input, we can check the format of the input element-coefficient pairs
    This is done by checking if the first character of each element-coefficient pair, splitting it into groupings of letters and numbers
    using the sepreate_string_number function
    If the input is of the correct format there will be two entries in the list, the first for the coefficient and the second for the element symbol
    Effectively this ensures that after splitting the input on the +'s all that is left is a list of element-coefficient pairs that are in the correct format
    """
    correct_format_check_success = False # This variable is used to check if the format check was successful. At the end of the function it is returned.
    error_detection = 0 # This variable is used to check if any errors have been detected. If it is 0 at the end of the function, the format check was successful.
    for i in user_input:
        if i == '':
            print("Empty element detected. Please try again.")
            error_detection += 1
            break
            # This for loop checks if any of the element-coefficient pairs are empty. If they are, it prints an error message and increments the error detection variable.
        letter_and_number_list = seperate_string_number(i) # The seperate_string_number function is called on each element-coefficient pair in the user input.
        # For an ideal user input this will return a list of two entries, the first being the coefficient and the second being the element symbol.
        # This function only checks that each entry comprised of a string of numbers followed by a string of letters.
        if len(letter_and_number_list) != 2:
            print(f'{i} is not a valid entry. Entries must come in integer-element pairs e.g "1H" or "2O". Please try again.')
            error_detection += 1
            # If the list returned by the seperate_string_number function is not of length 2, it means that the element-coefficient pair is not in the correct format.
            # An error message is printed and the error detection variable is incremented and the loop is broken.
            
        elif letter_and_number_list[0].isnumeric() == False:
            print(f'{i} is not a valid entry. Entries must come in integer-element pairs e.g "1H" or "2O". Please try again.')
            error_detection += 1
            # If the first entry in the list returned by the seperate_string_number function is not numeric, it means that the element-coefficient pair is not in the correct format.
            # An error message is printed and the error detection variable is incremented and the loop is broken.
             
        elif letter_and_number_list[1].isalpha() == False:
            print(f'{i} is not a valid entry. Entries must come in integer-element pairs e.g "1H" or "2O". Please try again.')
            error_detection += 1
            # If the second entry in the list returned by the seperate_string_number function is not alphabetic, it means that the element-coefficient pair is not in the correct format.
            # An error message is printed and the error detection variable is incremented and the loop is broken.
            
        elif letter_and_number_list[0][0] == '0':
            print('Your coefficient starts with a 0. Please try again.')
            error_detection += 1
            # If the first entry in the list returned by the seperate_string_number function is 0, it means that the element-coefficient pair is not in the correct format.
            # An error message is printed and the error detection variable is incremented and the loop is broken.  
            # Also checks if coefficient starts with 0.       
    if error_detection == 0:
        correct_format_check_success = True
        # If the error detection variable is 0 at this stage, no errors were detected. The format check was successful and the check_success variable is set to True.
    return user_input, correct_format_check_success

def distinct_symbol_check(user_input):
    """
    This function checks that the user input contains no duplicate element symbols. It does this by adding every new
    element new symbol to a list and if the symbol is already in the list it will print an error message
    """
    distinct_symbol_check_success = False # This variable is used to check if the distinct symbol check was successful. At the end of the function it is returned.
    distinct_symbol_list = [] # This list is used to store all the dinstinct element symbols in the user input.
    error_detection = 0 # This variable is used to check if any errors have been detected. If it is 0 at the end of the function, the distinct symbol check was successful.
    for i in user_input:
        letter_and_number_list = seperate_string_number(i)
        if letter_and_number_list[1].lower() not in distinct_symbol_list:
            distinct_symbol_list.append(letter_and_number_list[1].lower())
            # If the element symbol is not in the distinct symbol list, it is added to the list.
            # The element symbol is converted to lower case to ensure that the same element symbol is not added twice.
        else:
            print(f"Duplicate element symbols detected ({letter_and_number_list[1].lower().capitalize()})")
            error_detection += 1
            # If the element symbol is already in the distinct symbol list, an error message is printed and the error 
            # detection variable is incremented.
            
    if error_detection == 0:
        distinct_symbol_check_success = True  
        # If the error detection variable is 0 at this stage, no errors were detected. The distinct symbol check was 
        # successful and the check_success variable is set to True.
    else: 
        print("Please try again.") 
        # If the error detection variable is not 0 at this stage, an error message has already been printed and the user 
        # is promted to try again.

    return user_input, distinct_symbol_check_success, distinct_symbol_list

def element_symbol_check(distinct_symbol_list):
    """
    This function checks that the user input only contains valid element symbols. It does this by simply comparing the string 
    section of the coefficient-element pair to a list of valid element symbols
    """
    element_symbol_check_success = False
    feasible_elements = ['h','he','li','be','b','c','n','o','f','ne'] 
    error_detection = 0
    for i in distinct_symbol_list:
        if i.lower() not in feasible_elements:
            print(f"{i} is not a valid element symbol. Please try again.")
            error_detection += 1
            break
        # This function utilises the distinct symbol list created in the distinct_symbol_check function.
        # This loop checks that each element symbol in the distinct symbol list is in the list of valid element symbols.
        # If it is not, an error message is printed and the error detection variable is incremented.
    if error_detection == 0:
        element_symbol_check_success = True
        # If the error detection variable is 0 at this stage, no errors were detected. The element symbol check was 
        # successful and the check_success variable is set to True.
    return element_symbol_check_success


def seperate_string_number(input):
    """
    This function takes a string and splits it into a list of strings of numbers and letters. It does this by checking if the character is 
    of the same type to the previous character, if it is the loop carries on and if not it adds the character to a new string in the list
    and starts again 
    """
    
    previous_character = input[0]
    groups = [] # This list will contain the groupings of numbers and letters.
    newword = input[0] # The first character in the input string is added to the newword variable
    for x, i in enumerate(input[1:]):
        # This loop starts at the second character in the input string and loops through the rest of the string.
        if i.isalpha() and previous_character.isalpha():
            newword += i        
        elif i.isnumeric() and previous_character.isnumeric():
            newword += i
        # If the current character is the same type as the previous character, it is added to the newword variable.
        else:
            groups.append(newword)
            newword = i
        # If the current character is not the same type as the previous character, the newword variable is added 
        # to the groups list and the newword variable is reset to the current character.

        previous_character = i
        # The previous character variable is updated to the current character.

        if x == len(input) - 2:
            groups.append(newword)
            newword = ''
        # This if statement checks if the loop is on the last character in the input string. If it is, the newword 
        # variable is added to the groups list and the newword variable is reset to an empty string.
    return groups


def chemical_formula_builder(user_input):
    """
    This function takes the user input and builds the chemical formula aswell as making sure no coefficients = 1
    """
    chemical_formula = ""
    for i in user_input:
        letter_and_number_list = seperate_string_number(i)
        # This function utilises the seperate_string_number function to seperate the coefficient and element symbol.
        if letter_and_number_list[0] == '1':
            chemical_formula += letter_and_number_list[1].capitalize()
            # If the coefficient is 1, only the element symbol is added to the chemical formula.
        else:
            chemical_formula += letter_and_number_list[1].capitalize() + letter_and_number_list[0]
            # If the coefficient is not 1, the element symbol and coefficient are added to the chemical formula in that order.

    return chemical_formula

def atomic_mass_calculator(user_input):
    """
    This function takes the user input and calculates the atomic mass of the compound
    """
    atomic_masses = {'h':1,'he':4,'li':7,'be':9,'b':11,'c':12,'n':14,'o':16,'f':19,'ne':20}
    # This dictionary contains the atomic masses of all the allowed elements.
    atomic_mass = 0
    for i in user_input:
        letter_and_number_list = seperate_string_number(i)
        atomic_mass += atomic_masses[letter_and_number_list[1].lower()]*int(letter_and_number_list[0])
        # This function utilises the seperate_string_number function to seperate the coefficient and element symbol.
        # The atomic mass of the element, which is collected from the dictionary, 
        # is multiplied by the coefficient and added to the atomic mass variable.
    return atomic_mass



