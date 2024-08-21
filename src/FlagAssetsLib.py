## @file FlagAssetsLib.py
#  @title FlagAssetsLib
#  @brief A library of constants and symbol/design options
#  @author Akram Hannoufa, Nathaniel Hu
#  @date 2022-03-31

# @var BASE_STRIPE_STYLES
#  Possible base stripe styles a flag can have
BASE_STRIPE_STYLES = ['NONE', 'HORIZONTAL',
                      'VERTICAL', 'CROSS', 'SALTIRE', 'CROSS_SALTIRE']

# @var OVERLAY_STRIPE_STYLES
#  Possible overlay stripe styles a flag can have;
#  applies only to singular horizontal and vertical stripes
OVERLAY_STRIPE_STYLES = ['NONE', 'HORIZONTAL_THIN', 'VERTICAL_THIN',
                         'CROSS_THIN', 'SALTIRE_THIN', 'CROSS_SALTIRE_THIN']

# @var STRIPE_NUMBER
#  Possible number of stripes a flag can have;
#  applies only to vertical and horizontal base stripes
STRIPE_NUMBER = ['ONE', 'TWO', 'THREE', 'SIX', 'TWELVE']

# @var SYMBOL_LOCATION
#  Possible locations a symbol can be placed on a flag
SYMBOL_LOCATION = ['TOP_LEFT', 'CENTER', 'TOP_RIGHT']

# @var SYMBOL_NUMBER
#  Possible number of symbols a flag can have
SYMBOL_NUMBER = ['ONE', 'TWO']

# @var SYMBOL_TYPES
#  Possible symbol types
SYMBOL_TYPES = ['NONE', 'MOON', 'ROUNDEL', 'SWORD']

# @var colours2rgb
#  maps the settings colour options to the RGB values tuple
colours2rgb = {'RED': (255, 0, 0), 'GREEN': (0, 255, 0), 'BLUE': (
    0, 0, 255), 'YELLOW': (255, 255, 0), 'PURPLE': (127, 0, 255)}

# @var low_res_flag_assets
#  Loads in all low resolution flag assets
low_res_flag_assets = {"VERTICAL": {"ONE": "jka/low_res/vstripe_1.jka",
                                    "TWO": "jka/low_res/vstripe_2.jka",
                                    "THREE": "jka/low_res/vstripe_3.jka",
                                    "SIX": "jka/low_res/vstripe_6.jka",
                                    "TWELVE": "jka/low_res/vstripe_12.jka",
                                    "ONE_THIN":
                                    "jka/low_res/vstripe_1_thin.jka"},
                       "HORIZONTAL": {"ONE": "jka/low_res/hstripe_1.jka",
                                      "TWO": "jka/low_res/hstripe_2.jka",
                                      "THREE": "jka/low_res/hstripe_3.jka",
                                      "SIX": "jka/low_res/hstripe_6.jka",
                                      "TWELVE":
                                      "jka/low_res/hstripe_12.jka",
                                      "ONE_THIN":
                                      "jka/low_res/hstripe_1_thin.jka"},
                       "SALTIRE": "jka/low_res/saltire.jka",
                       "CROSS": "jka/low_res/cross.jka",
                       "CROSS_SALTIRE": "jka/low_res/cross_saltire.jka",
                       "SALTIRE_THIN": "jka/low_res/saltire_thin.jka",
                       "CROSS_THIN": "jka/low_res/cross_thin.jka",
                       "CROSS_SALTIRE_THIN":
                       "jka/low_res/cross_saltire_thin.jka",
                       "MOON": "jka/low_res/moon.jka",
                       "SWORD": "jka/low_res/sword.jka",
                       "ROUNDEL": "jka/low_res/roundel.jka"}

# @var mid_res_flag_assets
#  Loads in all mid resolution flag assets
mid_res_flag_assets = {"VERTICAL": {"ONE": "jka/mid_res/vstripe_1.jka",
                                    "TWO": "jka/mid_res/vstripe_2.jka",
                                    "THREE": "jka/mid_res/vstripe_3.jka",
                                    "SIX": "jka/mid_res/vstripe_6.jka",
                                    "TWELVE": "jka/mid_res/vstripe_12.jka",
                                    "ONE_THIN":
                                    "jka/mid_res/vstripe_1_thin.jka"},
                       "HORIZONTAL": {"ONE": "jka/mid_res/hstripe_1.jka",
                                      "TWO": "jka/mid_res/hstripe_2.jka",
                                      "THREE": "jka/mid_res/hstripe_3.jka",
                                      "SIX": "jka/mid_res/hstripe_6.jka",
                                      "TWELVE": "jka/mid_res/hstripe_12.jka",
                                      "ONE_THIN":
                                      "jka/mid_res/hstripe_1_thin.jka"},
                       "SALTIRE": "jka/mid_res/saltire.jka",
                       "CROSS": "jka/mid_res/cross.jka",
                       "CROSS_SALTIRE": "jka/mid_res/cross_saltire.jka",
                       "SALTIRE_THIN": "jka/mid_res/saltire_thin.jka",
                       "CROSS_THIN": "jka/mid_res/cross_thin.jka",
                       "CROSS_SALTIRE_THIN":
                       "jka/mid_res/cross_saltire_thin.jka",
                       "MOON": "jka/mid_res/moon.jka",
                       "SWORD": "jka/mid_res/sword.jka",
                       "ROUNDEL": "jka/mid_res/roundel.jka"}

# @var high_res_flag_assets
#  Loads in all high resolution flag assets
high_res_flag_assets = {"VERTICAL": {"ONE": "jka/high_res/vstripe_1.jka",
                                     "TWO": "jka/high_res/vstripe_2.jka",
                                     "THREE": "jka/high_res/vstripe_3.jka",
                                     "SIX": "jka/high_res/vstripe_6.jka",
                                     "TWELVE": "jka/high_res/vstripe_12.jka",
                                     "ONE_THIN":
                                     "jka/high_res/vstripe_1_thin.jka"},
                        "HORIZONTAL": {"ONE": "jka/high_res/hstripe_1.jka",
                                       "TWO": "jka/high_res/hstripe_2.jka",
                                       "THREE": "jka/high_res/hstripe_3.jka",
                                       "SIX": "jka/high_res/hstripe_6.jka",
                                       "TWELVE": "jka/high_res/hstripe_12.jka",
                                       "ONE_THIN":
                                       "jka/high_res/hstripe_1_thin.jka"},
                        "SALTIRE": "jka/high_res/saltire.jka",
                        "CROSS": "jka/high_res/cross.jka",
                        "CROSS_SALTIRE": "jka/high_res/cross_saltire.jka",
                        "SALTIRE_THIN": "jka/high_res/saltire_thin.jka",
                        "CROSS_THIN": "jka/high_res/cross_thin.jka",
                        "CROSS_SALTIRE_THIN":
                        "jka/high_res/cross_saltire_thin.jka",
                        "MOON": "jka/high_res/moon.jka",
                        "SWORD": "jka/high_res/sword.jka",
                        "ROUNDEL": "jka/high_res/roundel.jka"}
