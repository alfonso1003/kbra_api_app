"""Font dictionary

Each letter (A-Z), number (0-9), and space character is
represented by an array of five strings containing zeros and
ones. When stacked on top of each other, those strings
provide a template for generating the corresponding character
as ASCII art. Simply replace the ones with a fill character
and the zeros with spaces.

Example:

In the font dictionary, the letter A looks like this:

['0110', '1001', '1111', '1001', '1001']

Stacking these strings on top of each other, then replacing
the zeros with spaces and the ones with the fill character X
would look like this:

'0110'  =>  ' 11 '  =>  ' XX '
'1001'  =>  '1  1'  =>  'X  X'
'1111'  =>  '1111'  =>  'XXXX'
'1001'  =>  '1  1'  =>  'X  X'
'1001'  =>  '1  1'  =>  'X  X'
"""
font = {
    "A": ["0110", "1001", "1111", "1001", "1001"],
    "B": ["1110", "1001", "1110", "1001", "1110"],
    "C": ["0110", "1001", "1000", "1001", "0110"],
    "D": ["1110", "1001", "1001", "1001", "1110"],
    "E": ["1111", "1000", "1110", "1000", "1111"],
    "F": ["1111", "1000", "1110", "1000", "1000"],
    "G": ["0111", "1000", "1011", "1001", "0110"],
    "H": ["1001", "1001", "1111", "1001", "1001"],
    "I": ["1", "1", "1", "1", "1"],
    "J": ["1111", "0010", "0010", "1010", "0100"],
    "K": ["1001", "1010", "1100", "1010", "1001"],
    "L": ["100", "100", "100", "100", "111"],
    "M": ["10001", "11011", "10101", "10001", "10001"],
    "N": ["1001", "1101", "1011", "1001", "1001"],
    "O": ["0110", "1001", "1001", "1001", "0110"],
    "P": ["1110", "1001", "1110", "1000", "1000"],
    "Q": ["0110", "1001", "1001", "1101", "0111"],
    "R": ["1110", "1001", "1110", "1010", "1001"],
    "S": ["0111", "1000", "0110", "0001", "1110"],
    "T": ["111", "010", "010", "010", "010"],
    "U": ["1001", "1001", "1001", "1001", "0110"],
    "V": ["1001", "1001", "1001", "0110", "0100"],
    "W": ["10001", "10101", "10101", "11011", "10001"],
    "X": ["10001", "01010", "00100", "01010", "10001"],
    "Y": ["10001", "01010", "00100", "00100", "00100"],
    "Z": ["1111", "0001", "0110", "1000", "1111"],
    "1": ["010", "110", "010", "010", "111"],
    "2": ["0110", "1001", "0010", "0100", "1111"],
    "3": ["1110", "0001", "0110", "0001", "1110"],
    "4": ["1001", "1001", "1111", "0001", "0001"],
    "5": ["1111", "1000", "0110", "0001", "1110"],
    "6": ["0110", "1000", "1110", "1001", "0110"],
    "7": ["1111", "0001", "0010", "0100", "0100"],
    "8": ["0110", "1001", "0110", "1001", "0110"],
    "9": ["0110", "1001", "0111", "0001", "0110"],
    "0": ["0110", "1001", "1001", "1001", "0110"],
    "space": ["0", "0", "0", "0", "0"],
}


def pixelate(text, fill):
    """Convert text to ASCII art using fill character

    Args:
        text (`str`): String to convert to ASCII art
        fill (`str`): Fill character to use

    Returns:
        `str`: ASCII art string (with line breaks)
    """

    # Write your code here
    char_list = []
    for chr in [*text.upper()]:
        if chr == " ":
            chr = "space"
        char_list.append(font.get(chr))

    final_word = ""
    for x in range(0, 5):
        for cl in char_list:
            final_word += cl[x]
            final_word += " "
        final_word += "\n"

    return format_character_parts(final_word, fill)


def format_character_parts(character_part, fill):
    return character_part.replace("0", " ").replace("1", fill)


print(pixelate("1 plus 2 equals 3", "*"))
