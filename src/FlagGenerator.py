## @file FlagGenerator.py
#  @title FlagGenerator
#  @brief A module for generating the flag image using a given input string
#         and hashing algorithm
#  @details FlagGenerator module, uses HashGenerator, HashToFlag and JKAReader
#           modules; no exported constants or types, no state or environment
#           variables, no state invariant or assumptions
#  @author Nathaniel Hu, Akram Hannoufa
#  @date 2022-04-07

from PIL import Image
from FlagAssetsLib import *

from HashGenerator import hash_generator
from HashToFlag import *
from JKAReader import parse_jka_file


## @brief FlagGenerator is a class that implements and encapsulates various
#         attributes and methods needed to generate the flag image files
#  @details the FlagGenerator contains the user settings and flag colours,
#           stripe info, symbol info, dimensions, image and pixel data


class FlagGenerator():

    ## @brief constructor method for FlagGenerator
    #  @details the attributes will be used to temporarily store the data
    #           needed to generate each flag image; overwritten with each flag
    #           subsequently generated
    def __init__(self):
        self.settings = dict()
        self.colours = ()
        self.stripe_info = ()
        self.symbol_info = ()
        self.width = 0
        self.height = 0
        self.flag_image = ()
        self.flag_pixels = ()

    ## @brief generates the flag image file using the given hash input string
    #        and input hash type string
    #  @details uses functions to get the flag data from the hash input string
    #           and input hash type string and stacks the flag asset layers to
    #           generate the final flag image saved to the gallery
    #  @param hash_input a string that will be run through the given hashing
    #                    algorithm to get a hexidecimal hashing digest
    #  @param hash_type a string representing the selected hashing algorithm;
    #                   default hashing algorithm is sha256
    #  @param settings a dictionary representing the user selected settings;
    #                  default resolution is high
    #                  default colours and symbol type
    #                  are randomly generated,
    #                  i.e. taken from generated flag data
    def generate_flag(self, hash_input, hash_type="SHA256",
                      settings={"RESOLUTION": "HIGH", "BASE_COLOUR": "RANDOM",
                                "SYMBOL_COLOUR": "RANDOM",
                                "SYMBOL_TYPE": "RANDOM"}):
        # print(settings) # for debugging
        self.settings = settings
        # generating flag data
        self.generate_flag_data(hash_input, hash_type.lower())

        # initializing flag image dimensions
        self._set_flag_dimensions()

        # @var flag_image
        #  initializing variable for storing
        #  image file data for set resolution
        self.flag_image = Image.new("RGB", (self.width, self.height))

        # loading all the pixels
        # @var flag_pixels
        #  the list storing the RGB colour values of each pixel in the image
        #  stored in flag_image
        self.flag_pixels = self.flag_image.load()

        # set base colour for generated flag image
        self._set_flag_base_colour()

        # set base stripes colour and style for generated flag image
        self._set_flag_base_stripes()

        # set overlay stripes colour and style for generated flag image
        self._set_flag_overlay_stripes()

        # set symbol type and colour for generated flag image
        self._set_flag_symbol()

        # save generated flag image as .png image file
        self._save_flag_image(hash_input)

    ## @brief generates the flag data using the given hash input string
    #        and input hash type string
    #  @details uses external functions to generate the flag data
    #           from the hash input string and input hash type string
    #  @param hash_input a string that will be run through the given hashing
    #                    algorithm to get a hexidecimal hashing digest
    #  @param hash_type a string representing the selected hashing algorithm
    def generate_flag_data(self, hash_input, hash_type):
        # @var hash_code
        #  the hexidecimal hash digest generated using the input hash string
        #  and input hash type string
        hash_code = pad_hashcode(hash_generator(hash_input, hash_type))
        # @var colours
        #  a list of five (R, G, B) colour tuples
        #  generated using the aforementioned generated hash digest
        self.colours = grind_hash_for_colors(hash_code)
        # @var stripe_info
        #  a tuple of the stripe style and number generated
        #  using the aforementioned generated hash digest
        self.stripe_info = (grind_hash_for_base_stripe_style(hash_code),
                            grind_hash_for_stripe_number(hash_code),
                            grind_hash_for_overlay_stripe_style(hash_code))
        # @var symbol_info
        #  a tuple of the symbol location, number and type generated using the
        #  aforementioned generated hash digest
        self.symbol_info = (grind_hash_for_symbol_locations(hash_code),
                            grind_hash_for_symbol_number(hash_code),
                            grind_hash_for_symbol_types(hash_code))
        # print(hash_code)
        # print(symbol_info[2])

    ## @brief sets dimensions for the generated flag image
    #  @details sets flag image width and height (in pixels) based upon the
    #           set resolution
    def _set_flag_dimensions(self):
        if self.settings["RESOLUTION"] == "LOW":
            self.width, self.height = 60, 40
        elif self.settings["RESOLUTION"] == "MID":
            self.width, self.height = 120, 80
        else:
            self.width, self.height = 240, 160

    ## @brief sets base colour for the generated flag image
    #  @details sets flag image base colour based on set colour choice (or if
    #           set to RANDOM, then sets to randomly generated colour)
    def _set_flag_base_colour(self):
        # selecting base colour (i.e. randomly generated or selected by user)
        base_colour = (0, 0, 0)
        if self.settings["BASE_COLOUR"] != "RANDOM":
            base_colour = colours2rgb[self.settings["BASE_COLOUR"]]
        else:
            base_colour = self.colours[0]
        # adding base colour layer
        for x1 in range(self.width):
            for y1 in range(self.height):
                self.flag_pixels[x1, y1] = base_colour

    ## @brief sets base stripes colour and style for the generated flag image
    #  @details sets flag image base stripes colour to randomly generated
    #           colour and base stripes style to randomly chosen stripes style
    def _set_flag_base_stripes(self):
        # selecting base stripes style
        if self.stripe_info[0] != "NONE":
            base_stripe_pixel_map = []
            # for regular horizontal and vertical stripes
            if self.stripe_info[0] == "VERTICAL" or (
                    self.stripe_info[0] == "HORIZONTAL"):
                if self.settings["RESOLUTION"] == "LOW":
                    base_stripe_pixel_map = parse_jka_file(
                        low_res_flag_assets[self.stripe_info[0]]
                        [self.stripe_info[1]])
                elif self.settings["RESOLUTION"] == "MID":
                    base_stripe_pixel_map = parse_jka_file(
                        mid_res_flag_assets[self.stripe_info[0]]
                        [self.stripe_info[1]])
                else:
                    base_stripe_pixel_map = parse_jka_file(
                        high_res_flag_assets[self.stripe_info[0]]
                        [self.stripe_info[1]])
            # for regular cross, saltire and cross_saltire stripes
            else:
                if self.settings["RESOLUTION"] == "LOW":
                    base_stripe_pixel_map = parse_jka_file(
                        low_res_flag_assets[self.stripe_info[0]])
                elif self.settings["RESOLUTION"] == "MID":
                    base_stripe_pixel_map = parse_jka_file(
                        mid_res_flag_assets[self.stripe_info[0]])
                else:
                    base_stripe_pixel_map = parse_jka_file(
                        high_res_flag_assets[self.stripe_info[0]])
            # adding flag base stripes layer
            for (x1, y1) in base_stripe_pixel_map:
                self.flag_pixels[x1, y1] = self.colours[1]

    ## @brief sets overlay stripes colour and style for the generated flag
    #         image
    #  @details sets flag image overlay stripes colour to randomly generated
    #           colour and overlay stripes style
    #           to randomly chosen stripes style
    def _set_flag_overlay_stripes(self):
        # selecting overlay stripes style
        if self.stripe_info[2] != "NONE":
            overlay_stripe_pixel_map = []
            # for thin vertical stripe
            if self.stripe_info[2] == "VERTICAL_THIN":
                if self.settings["RESOLUTION"] == "LOW":
                    overlay_stripe_pixel_map = parse_jka_file(
                        low_res_flag_assets["VERTICAL"]["ONE_THIN"])
                elif self.settings["RESOLUTION"] == "MID":
                    overlay_stripe_pixel_map = parse_jka_file(
                        mid_res_flag_assets["VERTICAL"]["ONE_THIN"])
                else:
                    overlay_stripe_pixel_map = parse_jka_file(
                        high_res_flag_assets["VERTICAL"]["ONE_THIN"])
            # for thin horizontal stripe
            elif self.stripe_info[2] == "HORIZONTAL_THIN":
                if self.settings["RESOLUTION"] == "LOW":
                    overlay_stripe_pixel_map = parse_jka_file(
                        low_res_flag_assets["HORIZONTAL"]["ONE_THIN"])
                elif self.settings["RESOLUTION"] == "MID":
                    overlay_stripe_pixel_map = parse_jka_file(
                        mid_res_flag_assets["HORIZONTAL"]["ONE_THIN"])
                else:
                    overlay_stripe_pixel_map = parse_jka_file(
                        high_res_flag_assets["HORIZONTAL"]["ONE_THIN"])
            # for thin cross, saltire and cross_saltire stripes
            else:
                if self.settings["RESOLUTION"] == "LOW":
                    overlay_stripe_pixel_map = parse_jka_file(
                        low_res_flag_assets[self.stripe_info[2]])
                elif self.settings["RESOLUTION"] == "MID":
                    overlay_stripe_pixel_map = parse_jka_file(
                        mid_res_flag_assets[self.stripe_info[2]])
                else:
                    overlay_stripe_pixel_map = parse_jka_file(
                        high_res_flag_assets[self.stripe_info[2]])
            # adding flag overlay stripes layer
            for (x1, y1) in overlay_stripe_pixel_map:
                self.flag_pixels[x1, y1] = self.colours[3]

    ## @brief sets symbol colour and type for the generated flag image
    #  @details sets flag image symbol type based on set symbol type choice
    #           (or if set to RANDOM, then sets to randomly selected symbol
    #           type); sets flag image symbol colour based on set symbol
    #           colour choice (or if set to RANDOM, then sets to randomly
    #           generated colour)
    def _set_flag_symbol(self):
        # selecting flag symbol and colour
        if self.symbol_info[2] != "NONE" or (
                self.settings["SYMBOL_TYPE"] != "NONE"):
            symbol_pixel_map = []
            symbol_colour = (0, 0, 0)
            # selecting symbol colour
            # (i.e. randomly selected or selected by user)
            if self.settings["SYMBOL_COLOUR"] != "RANDOM":
                symbol_colour = colours2rgb[self.settings["SYMBOL_COLOUR"]]
            else:
                symbol_colour = self.colours[2]
            # selecting symbol (i.e. randomly generated or selected by user)
            if self.settings["SYMBOL_TYPE"] != "RANDOM" and (
                    self.settings["SYMBOL_TYPE"] != "NONE"):
                if self.settings["RESOLUTION"] == "LOW":
                    symbol_pixel_map = parse_jka_file(
                        low_res_flag_assets[self.settings["SYMBOL_TYPE"]])
                elif self.settings["RESOLUTION"] == "MID":
                    symbol_pixel_map = parse_jka_file(
                        mid_res_flag_assets[self.settings["SYMBOL_TYPE"]])
                else:
                    symbol_pixel_map = parse_jka_file(
                        high_res_flag_assets[self.settings["SYMBOL_TYPE"]])
            elif self.settings["SYMBOL_TYPE"] == "RANDOM" and (
                    self.symbol_info[2] != "NONE"):
                if self.settings["RESOLUTION"] == "LOW":
                    symbol_pixel_map = parse_jka_file(
                        low_res_flag_assets[self.symbol_info[2]])
                elif self.settings["RESOLUTION"] == "MID":
                    symbol_pixel_map = parse_jka_file(
                        mid_res_flag_assets[self.symbol_info[2]])
                else:
                    symbol_pixel_map = parse_jka_file(
                        high_res_flag_assets[self.symbol_info[2]])
            # adding flag symbol layer
            for (x1, y1) in symbol_pixel_map:
                self.flag_pixels[x1, y1] = symbol_colour

    ## @brief saves generated flag image
    #  @details saves generated flag image as png image file to flag gallery
    #           directory, using given hash_input to name the image file
    #  @param hash_input a string that will be used to name the generated flag
    #                    image file
    def _save_flag_image(self, hash_input):
        self.flag_image.save(f"generated_flags/flag_{hash_input}.png")
