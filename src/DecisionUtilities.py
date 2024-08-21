## @file DecisionUtilities.py
#  @title DecisionUtilities
#  @brief A collection of modules used by HashToFlag to grind
#         the hashcode and map decisions to arrays.
#  @author Akram Hannoufa
#  @date 2022-04-11

import math

# @var COLOR_QUANTITY
#  Number of colours to be generated for flag design options
COLOR_QUANTITY = 5

# @var HEX_COLOR_LEN
# Length of a color in hex.
HEX_COLOR_LEN = 6

# @var HEX_BASE
# Base of the hexadecimal number system.
HEX_BASE = 16

# @var MINIMUM_HASH_LEN
# To generate unique colors, hashes need to contain
# at least this many characters.
MINIMUM_HASH_LEN = COLOR_QUANTITY * HEX_COLOR_LEN

# @var ASPECT_CONTROL_LEN
# Length of hash characters to generate one option.
ASPECT_CONTROL_LEN = 6

# @var MAX_DECISION_VALUE
# Decimal representation of hexadecimal 'ffffff'
# as the maximum value for aspect decisions.
MAX_DECISION_VALUE = 16777215

# @var DEBUG
# Set True to generate debug output in this module.
DEBUG = False

## @brief Generates a padded hashcode if it is not the minimum required length.
#  @details Input string gets padded until it is long
#   enough to generate all required flag options.
#  @param hashcode a string of the input string's corresponding hashcode value.
#  @throws TypeError if hashcode is not string type
#  @return modified hashcode, a padded version of the input hashcode.


def pad_hashcode(hashcode):
    if (not (isinstance(hashcode, str))):
        raise TypeError("hashcode must be a string!")

    while (len(hashcode) < MINIMUM_HASH_LEN):
        chardiff = diff(len(hashcode), MINIMUM_HASH_LEN)
        if DEBUG:
            print("Hashcode: %r with length: %d is too small."
                  "Appending difference." % (
                   hashcode, len(hashcode)))
        hashcode += hashcode[:chardiff]
        if DEBUG:
            print("Hash is now: %r with length: %d" %
                  (hashcode, len(hashcode)))
    return hashcode

## @brief Generates a selection from an array.
#  @param source_list the list to make a selection from
#  @param index the index to take the selection.
#  @throws ValueError if index value is negative
#  @return choice, the option from the source_list that matches the index.


def choose_from_list(source_list, index):
    if(index < 0):
        raise ValueError("index number cannot be negative!")
    choice = ""
    for i in range(len(source_list)):
        if(i < index):
            choice = source_list[i]
    return choice

## @brief Maps a number to an index of an array
#  @param max_digitsum the maximum possible option
#  @param num_decisions the number of possible decisions
#  @param digitsum the digit to map within possible options
#  @throws ValueError if any param is negative
#  @return decision, float index of array to get decision from.


def map_decision(max_digitsum, num_decisions, digitsum):
    if(max_digitsum < 0 or num_decisions < 0 or digitsum < 0):
        raise ValueError("input parameters cannot be negative!")
    return (num_decisions / (float(max_digitsum) + 1)) * (float(digitsum) + 1)

## @brief Generates a list of shorter tokens from a given input string
#  @details Created strings are of a specified size, n
#  @param seq input string to break apart
#  @param length length of generated substrings
#  @return tokens, list of shorter substrings of length n


def split_sequence(seq, length):
    tokens = []
    while seq:
        tokens.append(seq[:length])
        seq = seq[length:]
    return tokens

## @brief Generates a tuple of an RGB colour from a hexadecimal number
#  @details hexvalue is length 6, with every 2 characters
#   being part of the RGB tuple
#  @param hexvalue hexadecimal value (length=6) to convert to RGB
#  @throws TypeError if hexvalue is not a string
#  @return RGB tuple, representing an RGB colour in integer values


def hex2rgb(hexvalue):
    if(not (isinstance(hexvalue, str))):
        raise TypeError("hexcode must be a string type")

    if ('#' in hexvalue):
        hexcolor = hexvalue.replace('#', '')
    else:
        hexcolor = hexvalue

    if (len(hexcolor) != 6):
        print("Unexpected length of hex color value."
              "\nSix characters excluding \'#\' expected.")
        return 0

    red = int(hexcolor[0:2], HEX_BASE)
    green = int(hexcolor[2:4], HEX_BASE)
    blue = int(hexcolor[4:6], HEX_BASE)

    return red, green, blue

## @brief Calculates the absolute difference of two float values
#  @param num1 first float value
#  @param num2 second float value
#  @return The integer value of the absolute difference between float values.


def diff(num1, num2):
    return int(math.fabs(num1 - num2))
