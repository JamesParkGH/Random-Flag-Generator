## @file JKAReader.py
#  @title JKAReader
#  @brief A library module for parsing .jka files for use in generating flags
#  @author Nathaniel Hu
#  @date 2022-02-26

filled_pixel = "#"
unfilled_pixel = "."

## @brief
#  @param
def parse_jka_file(filename):
    file_data = open(filename, 'r')

    pixel_map = []

    i = 0
    for line in file_data:
        j = 0
        for char in line:
            if char == filled_pixel:
                pixel_map.append((j, i))
            j += 1
        i += 1

    file_data.close()

    return pixel_map