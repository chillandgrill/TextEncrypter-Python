from random import randint

seed = []


def generate_seed():
    """
    Generate a seed to replace every ASCII character with
    two other ASCII characters, including whitespace, etc.
    """
    for char_id in range(128):
        while True:
            char_sequence = [chr(randint(0, 127)), chr(randint(0, 127))]
            if char_sequence not in seed:
                break
        seed.append(char_sequence)


def construct_file(in_file):
    offset_seed = randint(0, 127)

    generate_seed()

    write_to_file = "#encrypted "
    write_to_file += chr(offset_seed)
    print("".join(str(two_chars) for char_sequence in seed for two_chars in char_sequence))
    write_to_file += "".join(str(two_chars) for char_sequence in seed for two_chars in char_sequence)

    for letter in in_file:
        if ord(letter) + offset_seed >= 128:
            write_to_file += "".join(seed[ord(letter) + offset_seed - 128])
        else:
            write_to_file += "".join(seed[ord(letter) + offset_seed])

    return write_to_file
