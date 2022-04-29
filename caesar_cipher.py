

# Imports
from string import ascii_uppercase


# Functions
def cipher_key(shift):
    original_letters = ascii_uppercase
    shifted_letters = ascii_uppercase[int(shift):] + ascii_uppercase[:int(shift)]

    return dict(zip(original_letters, shifted_letters))


def shift_line(line, dict_key):
    new_line = ""
    for letter in line:
        if letter == " ":
            new_line += " "
            continue
        elif letter == "\n":
            new_line += "\n"
            continue
        elif not letter.isalpha():
            new_line += letter
            continue

        
        letter = letter.upper()
        new_line += dict_key[letter]

    return new_line


def encrypt_message(filename, dict_key):
    fixed = []
    final = ""
    with open(filename) as file:
        for line in file:
            fixed += shift_line(line,dict_key) # uses key to encrypt
        for lines in fixed:
            final = final + lines
        file = open("encrypted_{}".format(user_file),"w")
        file.write(final) # adds to final and writes in new .txt
        file.close()



# Main
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

key = cipher_key(shift_value)

encrypt_message(user_file, key)
