import os
from Encrypter.Encrypt import construct_file

file_list = os.listdir(os.getcwd())
print(file_list)

for file in file_list:
    if file.endswith(".txt"):
        working = open(file, "r")
        raw_file_text = working.read()
        working.close()
        working = open(file, "w")
        working.write(construct_file(raw_file_text))
        working.close()