import os
from Encrypter import Decrypt
from Encrypter import Encrypt

file_list = os.listdir(os.getcwd())

for i in range(0, 2):
    for file in file_list:
        if file.endswith(".txt"):
            working = open(file, "r")
            raw_file_text = working.read()
            working.close()

            working = open(file, "w")

            if raw_file_text.startswith("#encrypted"):
                Decrypt.init_string(raw_file_text)
                working.write(Decrypt.construct_file())

            else:
                working.write(Encrypt.construct_file(raw_file_text))
