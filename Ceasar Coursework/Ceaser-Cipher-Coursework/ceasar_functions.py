#Ceasar cipher functions
import random
import string
import numpy as np

def shift_key_selection():
    shift_key = input("How much do you want shift to be?")
    while True:
        if shift_key == 'random':
            break
        try:
            int(shift_key)
        except ValueError:
            print("This is an invalid entry")
            shift_key = input("How much do you want shift to be?")
        else:
            shift_key = int(shift_key)
            break
    if shift_key == 'random':
        shift_key = random.randint(1, 25)
        print(shift_key)
    return(shift_key) 

def encryption_mode():
    encryption_modes = ["encrypt","decrypt","auto-decrypt"]
    encryptionMode = input("Choose an encryption mode (encrypt/decrypt/auto-decrypt): ")
    while encryptionMode not in encryption_modes:
        print("This is not a valid selection. Please choose from the available options")
        encryptionMode = input("Choose an encryption mode:  ")
    return(encryptionMode)

def text_input():
    textInput = input("Enter some text to be encrypted/decrypted")
    while textInput.strip() == "":
        print("No message entered")
        textInput = input("Enter some text to be encrypted/decrypted")
    return(textInput)

def file_input():
    fileName = input("Enter the .txt file name")
    while True:
        try:     
            messageFile = open(f'{fileName}.txt','r')
        except FileNotFoundError:
            print("There is no .txt file with this name")
            fileName = input("Enter the file name")
        else:
            messageFile = open(f'{fileName}.txt','r')
            break
    messageFile = messageFile.read().upper()

    return(messageFile)

def input_selection():
    
    inputFormats = ["manual","text file"]
    input_format = input("What format is your input text in? (manual/text file)")
    while input_format not in inputFormats:
        print("This is is not a valid input format. Please choose from manual or text file")
        input_format = input("What format is your input text in? (manual/text file)")

    if input_format == "manual":
        textInput = text_input()
    if input_format == "text file":
        textInput = file_input()
    return(textInput)

def ceasar_encrypt(encryptText:str, shift:int): 
    cipherText = ""
    for ch in encryptText.upper():
        if ch.isalpha():
            encryptedLetter = ord(ch) + shift 
            if encryptedLetter > ord('Z'):
                encryptedLetter -= 26            
            cipherText += chr(encryptedLetter)
        else:
            cipherText += ch
    return(cipherText)

def ceasar_decrypt(decryptText:str, shift:int):
    cipherText = ""
    for ch in decryptText.upper():
        if ch.isalpha():
            encryptedLetter = ord(ch) - shift 
            if encryptedLetter < ord('A'):
                encryptedLetter += 26            
            cipherText += chr(encryptedLetter)
        else:
            cipherText += ch
    return(cipherText)

def ceasar_auto_decrypt(decryptText:str):
    word_file = open('words.txt','r')
    words = word_file.read().upper()
    words = words.split("\n")
    matched_keys = []
    userCheckOptions = ["Y","N"]
    userCheck = ""

    for shift_key in range(26):
        decryptTextSplit = ceasar_decrypt(decryptText,shift_key).split(" ")
        decryptTextSplitSection = decryptTextSplit[0:9]
        #print(decryptTextSplit)
        for element in decryptTextSplitSection:
            if element in words:
                matched_keys.append(shift_key)
                break
    print(f"Possible shift keys are {matched_keys}.")            
    for key in matched_keys:
        print(ceasar_decrypt(decryptText,key).split(" ")[0:9])        
        userCheck = input("Does this decryption look correct? (Y/N)")
        while userCheck not in userCheckOptions:
            print("This is not a valid selection. Please choose from the available options (Y/N)")
            userCheck = input("Does this decryption look correct? (Y/N)")       
        if userCheck == "Y":
            result = f"The decryption key is {key} and your decrypted message is - {ceasar_decrypt(decryptText,key)}"
            break
    if userCheck != "Y":
        result = "Unable to decrypt message."
        
    return(result)

def message_analysis_preperation(Text:str):
    lowerText = Text.translate(str.maketrans("","", string.punctuation))
    splitText = lowerText.lower().split()
    Text = ""
    for word in splitText:
        word = "".join(filter(lambda x: x.isalpha(), word))
        Text += f'{word} '     
    return(Text)

#print(ceasar_encrypt('hello my name is Jamie and i went shopping in a small shop looking for a big animal',6))
#print(ceasar_auto_decrypt('NKRRU SE TGSK OY PGSOK GTJ O CKTZ YNUVVOTM OT G YSGRR YNUV RUUQOTM LUX G HOM GTOSGR'))

#print(file_input())

