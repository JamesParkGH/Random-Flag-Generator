## @file HashToFlag.py
#  @title HashToFlag
#  @brief A module with functions for taking a given
#         hashcode input and generating the options for
#         the flag to be generated.
#  @details Uses DecisionsUtilities and FlagAssetsLib
#  @author Akram Hannoufa
#  @date 2022-03-15

from DecisionUtilities import *
from FlagAssetsLib import *


## @brief Generates the array of colours to be used in the flag generation.
#  @details Hex values of the hashcode are converted
#           to an RGB value for colour.
#  @param hashcode a string of the input string's corresponding hashcode value.
#  @return colors, an array of RGB values to be used by FlagGenerator.
def grind_hash_for_colors(hashcode):
    hashparts = split_sequence(hashcode, HEX_COLOR_LEN)
    colors = []
    for i in range(COLOR_QUANTITY):
        colors.append(hex2rgb(hashparts[i]))
    if DEBUG:
        print("Generated colors: %r" % colors)
    return colors

## @brief Generates the base stripe style to be used in flag generation.
#  @details Uses the first 6 characters of a hashcode to map to an array index
#           ,ie. the option to use for the desired aspect.
#  @param hashcode a string of the input string's corresponding hashcode value.
#  @return A base stripe style option.


def grind_hash_for_base_stripe_style(hashcode):
    stripe_style = hashcode[:ASPECT_CONTROL_LEN]
    hash_dec_value = int(stripe_style, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE, len(
        BASE_STRIPE_STYLES), hash_dec_value)
    return choose_from_list(BASE_STRIPE_STYLES, choice)

## @brief Generates the overlay stripe style to be used in flag generation.
#  @details Uses the first 6 characters of a hashcode to map to an array index
#    ,ie.the option to use for the desired aspect.
#  @param hashcode a string of the input string's corresponding hashcode value.
#  @return An overlay stripe style option.


def grind_hash_for_overlay_stripe_style(hashcode):
    stripe_style = hashcode[:ASPECT_CONTROL_LEN]
    hash_dec_value = int(stripe_style, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE, len(
        OVERLAY_STRIPE_STYLES), hash_dec_value)
    return choose_from_list(OVERLAY_STRIPE_STYLES, choice)

## @brief Generates the number of stripes to be used in flag generation.
#  @details Uses the second 6 characters of a hashcode to map to an array index
#           ,ie.the option to use for the desired aspect.
#  @param hashcode a string of the input string's corresponding hashcode value.
#  @return A stripe number option.


def grind_hash_for_stripe_number(hashcode):
    stripe_number = hashcode[ASPECT_CONTROL_LEN:(ASPECT_CONTROL_LEN * 2)]
    hash_dec_value = int(stripe_number, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE, len(
        STRIPE_NUMBER), hash_dec_value)
    return choose_from_list(STRIPE_NUMBER, choice)

##  @brief Generates the symbol location to be used in flag generation.
#  @details Uses the third 6 characters of a hashcode to map to an array index
#       ,ie.the option to use for the desired aspect.
#  @param hashcode a string of the input string's corresponding hashcode value.
#  @return A symbol location option.


def grind_hash_for_symbol_locations(hashcode):
    symbol_location = hashcode[(ASPECT_CONTROL_LEN*2):(ASPECT_CONTROL_LEN*3)]
    hash_dec_value = int(symbol_location, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE,
                          len(SYMBOL_LOCATION), hash_dec_value)
    return choose_from_list(SYMBOL_LOCATION, choice)

## @brief Generates the number of symbols to be used in flag generation.
#  @details Uses the fourth 6 characters of a hashcode to map to an array index
#           ,ie.the option to use for the desired aspect.
#  @param hashcode a string of the input string's corresponding hashcode value.
#  @return A symbol number option.


def grind_hash_for_symbol_number(hashcode):
    symbol_number = hashcode[(ASPECT_CONTROL_LEN * 3):(ASPECT_CONTROL_LEN * 4)]
    hash_dec_value = int(symbol_number, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE, len(
        SYMBOL_NUMBER), hash_dec_value)
    return choose_from_list(SYMBOL_NUMBER, choice)

## @brief Generates the symbol type to be used in flag generation.
#  @details Uses the fifth 6 characters of a hashcode to map to an array index,
#       ie.the option to use for the desired aspect.
#  @param hashcode a string of the input string's corresponding hashcode value.
#  @return A symbol type option.


def grind_hash_for_symbol_types(hashcode):
    symbol_type = hashcode[(ASPECT_CONTROL_LEN * 4):(ASPECT_CONTROL_LEN * 5)]
    hash_dec_value = int(symbol_type, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE,
                          len(SYMBOL_TYPES), hash_dec_value)
    return choose_from_list(SYMBOL_TYPES, choice)
