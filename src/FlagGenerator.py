## @file FlagGenerator.py
#  @title FlagGenerator
#  @brief A library module for generating the flag using a given input string
#         and hashing algorithm
#  @author Nathaniel Hu
#  @date 2022-02-26

from PIL import Image

from HashGenerator import hash_generator
from HashToFlag import (
    pad_hashcode, grind_hash_for_colors, grind_hash_for_stripe_style,
    grind_hash_for_stripe_number, grind_hash_for_symbol_locations,
    grind_hash_for_symbol_number, grind_hash_for_symbol_types
    )
from JKAReader import parse_jka_file

flag_assets = {"SALTIRE": "jka/saltire.jka", "CROSS": "jka/cross.jka", "MOON": "jka/moon.jka", "SWORD": "jka/sword.jka", "ROUNDEL": "jka/roundel.jka"}

def generate_flag(hash_input, hash_type):
    # generating flag data
    (colours, stripe_info, symbol_info) = generate_flag_data(hash_input, hash_type)
    flag_layers = []

    # creating flag image
    width, height = (60, 40)
    mode = 'RGB'
    flag_image = Image.new(mode, (width, height))
    
    # loading all the pixels
    flag_pixels = flag_image.load()

    # adding base colour layer
    for x in range(width):
        for y in range(height):
            flag_pixels[x, y] = colours[0]

    # adding flag stripes layer
    if stripe_info[0] == "NONE":
        pass

    # adding flag symbol layer
    symbol_pixel_map = parse_jka_file(flag_assets[symbol_info[2]])
    for (x, y) in symbol_pixel_map:
        flag_pixels[x, y] = colours[2]

    # show generated flag image
    # flag_image.show()

    # save generated flag image
    flag_filename = f"flag_{hash_input}.png"
    flag_filepath = f"generated_flags/{flag_filename}"
    flag_image.save(flag_filepath)

## @brief
#  @param
def generate_flag_data(hash_input, hash_type):
    hash_code = pad_hashcode(hash_generator(hash_input, hash_type))
    colours = grind_hash_for_colors(hash_code)
    stripe_info = (grind_hash_for_stripe_style(hash_code), grind_hash_for_stripe_number(hash_code))
    symbol_info = (grind_hash_for_symbol_locations(hash_code), grind_hash_for_symbol_number(hash_code),
                    grind_hash_for_symbol_types(hash_code))
    print(hash_code)
    print(symbol_info[2])
    return (colours, stripe_info, symbol_info)

if __name__ == "__main__":
    generate_flag("Sword is pointy", "sha256")

