import os
from Encrypter import Decrypt
from Encrypter import Encrypt

# Get a list of files in the current working directory (This is the part that limits this script to windows, as Unix OSes handle applications differently)
file_list = os.listdir(os.getcwd())

for file in file_list:
    if file.endswith(".txt"):
        working = open(file, "r") # Open the file in read mode, this is the part of code that limits the program to ANSI only.
        raw_file_text = working.read()
        working.close()

        working = open(file, "w") # Open the file in write mode. This completely wipes the file, and this causes data loss in the case of a bad read.

        if raw_file_text.startswith("#encrypted"): # Check to see if the current file is encrypted or not
            Decrypt.init_string(raw_file_text)
            working.write(Decrypt.construct_file())

        else:
            working.write(Encrypt.construct_file(raw_file_text))
