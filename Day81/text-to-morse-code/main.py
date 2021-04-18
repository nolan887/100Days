# You will use what you've learnt to create a text-based (command line) program that takes any String input and converts it into Morse Code.
#
# You've created plenty of text-based programs in Days 1 -10, so look back at some of those projects if you don't remember what a text-base program looks like.
#
# Wikipedia Entry for Morse Code
#
# The design, functionality, code style is all up to you. You're wearing the big-girl/big-boy pants now. So you get to decide.

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

converter_is_on = True

while converter_is_on:
    morse_string = ""
    to_translate = str(input("Text to translate to morse code: "))
    for letter in to_translate.upper():
        if letter == " ":
            morse_string += ""
        else:
            morse_string += MORSE_CODE_DICT[letter]
            morse_string += " "
    print(f"{to_translate} converted to morse code is: {morse_string}")