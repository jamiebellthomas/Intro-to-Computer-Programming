import random
from ceasar_functions import *

#encryptText = "Hello wOrlD1!?"
#decryptText = "MJqqT btWQi1?!"
#shift = 5

encryptionMode = encryption_mode()
textInput = input_selection()

if encryptionMode != "auto-decrypt":
    shift_key = shift_key_selection()

if encryptionMode == "encrypt":
    print(ceasar_encrypt(textInput, shift_key))
if encryptionMode == "decrypt":
    print(ceasar_decrypt(textInput, shift_key))
if encryptionMode == "auto-decrypt":
    print(ceasar_auto_decrypt(textInput))


