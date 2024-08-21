## @file JKAReader.py
#  @title JKAReader
#  @brief A library module for parsing .jka files for use in generating flags
#  @details JKAReader module, uses no other modules; exported constants
#           FILLED_PIXEL and UNFILLED_PIXEL, no exported types, no state or
#           environment variables, no state invariant, assumption that input
#           .jka file exists in the flag assets directory
#  @author Nathaniel Hu
#  @date 2022-04-07

from os.path import exists


# @var FILLED_PIXEL
#  exported type representing a filled pixel for a flag asset
FILLED_PIXEL = "#"
# @var UNFILLED_PIXEL
#  exported type representing an unfilled pixel for a flag asset
UNFILLED_PIXEL = "."


## @brief parses the input flag asset (.jka) file data into a pixel map
#  @details parses the file data by pixel and adds filled pixels to the pixel
#           map
#  @param filename a string representing the name of the flag asset (.jka)
#         file that contains the flag asset pixel map data
#  @return a list containing the (x, y) coordinates of all filled pixels for
#          the given flag asset
def parse_jka_file(filename):
    # @var pixel_map
    #  a list containing the (x, y) coordinates of all filled pixels found
    #  from parsing the pixel map data
    pixel_map = []

    # checks if given file exists
    if exists(filename):
        # @var file_data
        #  the variable storing the input (.jka) data file reference
        file_data = open(filename, 'r')

        # iterates through file and extracts pixel position data
        pixel1 = 0
        for line in file_data:
            pixel2 = 0
            for char in line:
                if char == FILLED_PIXEL:
                    pixel_map.append((pixel2, pixel1))
                pixel2 += 1
            pixel1 += 1

        file_data.close()

    return pixel_map
