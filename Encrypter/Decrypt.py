from string import printable

seed = []
offset = 0
in_file = None


def init_string(raw_text):
    """
    Read in the string provided by main, determine the
    seed offset and delete extraneous characters
    """
    global in_file
    in_file = raw_text
    in_file = in_file[10:]

    global offset
    offset = printable.index(in_file[1])
    in_file = in_file[0:]


def parse_seed():
    seed_as_string = in_file[:(len(printable) * 2)]

    for i in range(0, len(printable) * 2, 2):
        two_chars = [seed_as_string[i], seed_as_string[i + 1]]
        seed.append(two_chars)


def construct_file():
    parse_seed()

    write_to_file = ""
    global in_file

    in_file = in_file[len(printable) * 2 + 2:]

    for i in range(0, len(in_file), 2):
        two_chars = [in_file[i], in_file[i + 1]]
        if seed.index(two_chars) - offset < 0:
            write_to_file += printable[int(seed.index(two_chars)) - offset + len(printable) - 1]
        else:
            write_to_file += printable[int(seed.index(two_chars)) - offset - 1]
    return write_to_file
