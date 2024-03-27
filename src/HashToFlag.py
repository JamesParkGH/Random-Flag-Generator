import math

COLOR_QUANTITY = 5
#stripe 1 color, stripe 2 color, logo 1 color, logo 2 color

# Length of a color in hex.
HEX_COLOR_LEN = 6

# Base of the hexadecimal number system.
HEX_BASE = 16

# To generate unique colors, hashes need to
# contain at least this many characters.
MINIMUM_HASH_LEN = COLOR_QUANTITY * HEX_COLOR_LEN

# The first and second six characters of a hash
# determine the avatars overall aspect.
ASPECT_CONTROL_LEN = 6

# Decimal representation of hexadecimal 'ffffff'
# as the maximum value for aspect decisions.
MAX_DECISION_VALUE = 16777215

# Set True to generate debug output in this module.
DEBUG = False

STRIPE_STYLE = ['HORIZONTAL', 'VERTICAL', 'NONE']

STRIPE_NUMBER = ['ZERO', 'TWO', 'THREE', 'SIX', 'TWELVE']

SYMBOL_LOCATION = ['TOP_LEFT', 'CENTER', 'TOP_RIGHT']


SYMBOL_NUMBER = ['ZERO','ONE', 'TWO']

SYMBOL_TYPES = ['MOON', 'ROUNDEL', 'SWORD', 'CROSS', 'SALTIRE']

def init_combo_list():
    return
    #Possible stripe, symbol combos
def pad_hashcode(hashcode):
    while (len(hashcode) < MINIMUM_HASH_LEN):
        chardiff = diff(len(hashcode), MINIMUM_HASH_LEN)
        if DEBUG:
            print ("Hashcode: %r with length: %d is too small. Appending difference." % (hashcode, len(hashcode)))
        hashcode += hashcode[:chardiff]
        if DEBUG:
            print ("Hash is now: %r with length: %d" % (hashcode, len(hashcode)))
    return hashcode
def grind_hash_for_colors(hashcode):
    """Extracts information from the hashcode
    to generate different colors. Returns a
    list of colors in (r,g,b) tupels."""

    # When using smaller hash algorithms like MD5 or SHA1,
    # the number of bits does not provide enough information
    # to generate unique colors. Instead the hash is internally
    # appended by itself to fit the MINIMUM_HASH_LEN.
    # This leads to smaller hashes displaying less color
    # variatons, depicting the insecurity of small hashes.
    
    hashparts = split_sequence(hashcode, HEX_COLOR_LEN)

    colors = []

    for i in range(COLOR_QUANTITY):
        colors.append(hex2rgb(hashparts[i]))
    if DEBUG:
        print ("Generated colors: %r" % colors)
    return colors

def grind_hash_for_stripe_style(hashcode):
    #first 6 characters of hash determine this
    stripe_style = hashcode[:ASPECT_CONTROL_LEN]
    hash_dec_value = int(stripe_style, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE, len(STRIPE_STYLE), hash_dec_value)
    return choose_from_list(STRIPE_STYLE, choice)

def grind_hash_for_stripe_number(hashcode):
    #second 6 characters of hash determine this
    stripe_number = hashcode[ASPECT_CONTROL_LEN:(ASPECT_CONTROL_LEN * 2)]
    hash_dec_value = int(stripe_number, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE, len(STRIPE_NUMBER), hash_dec_value)
    return choose_from_list(STRIPE_NUMBER, choice)

def grind_hash_for_symbol_locations(hashcode):  
    #third 6 characters of hash determine this
    symbol_location = hashcode[(ASPECT_CONTROL_LEN * 2):(ASPECT_CONTROL_LEN * 3)]
    hash_dec_value = int(symbol_location, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE, len(SYMBOL_LOCATION), hash_dec_value)
    return choose_from_list(SYMBOL_LOCATION, choice)
    
def grind_hash_for_symbol_number(hashcode):
    #fourth 6 characters of hash determine this
    symbol_number = hashcode[(ASPECT_CONTROL_LEN * 3):(ASPECT_CONTROL_LEN * 4)]
    hash_dec_value = int(symbol_number, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE, len(SYMBOL_NUMBER), hash_dec_value)
    return choose_from_list(SYMBOL_NUMBER, choice)
    
def grind_hash_for_symbol_types(hashcode):
    #fifth 6 characters of hash determine this
    symbol_type = hashcode[(ASPECT_CONTROL_LEN * 4):(ASPECT_CONTROL_LEN * 5)]
    hash_dec_value = int(symbol_type, HEX_BASE)
    choice = map_decision(MAX_DECISION_VALUE, len(SYMBOL_TYPES), hash_dec_value)
    print(symbol_type)
    print(hash_dec_value)
    print(choice)
    return choose_from_list(SYMBOL_TYPES, choice)


def choose_from_list(source_list, index):
    choice = ""
    for i in range(len(source_list)):
        if(i < index):
            choice =  source_list[i]
    print(choice)
    return choice

def map_decision(max_digitsum, num_decisions, digitsum):
    """Maps the domain to a number of decisions."""
    return (num_decisions / (float(max_digitsum) + 1)) * (float(digitsum) + 1)

def split_sequence(seq, n):
    """Generates tokens of length n from a sequence.
    The last token may be of smaller length."""
    tokens = []
    while seq:
        tokens.append(seq[:n])
        seq = seq[n:]
    return tokens

def hex2rgb(hexvalue):
    """Converts a given hex color to
    its respective rgb color."""

    # Make sure a possible '#' char is eliminated
    # before processing the color.
    if ('#' in hexvalue):
        hexcolor = hexvalue.replace('#', '')
    else:
        hexcolor = hexvalue

    # Hex colors have a fixed length of 6 characters excluding the '#'
    # TODO: Include custom exception here, even if it should never happen.
    if (len(hexcolor) != 6):
        print ("Unexpected length of hex color value.\nSix characters excluding \'#\' expected.")
        return 0

    # Convert each two characters of
    # the hex to an RGB color value.
    r = int(hexcolor[0:2], HEX_BASE)
    g = int(hexcolor[2:4], HEX_BASE)
    b = int(hexcolor[4:6], HEX_BASE)

    return r, g, b


def diff(a, b):
    """Returns the difference between two values."""
    return int(math.fabs(a - b))


#horizontal stripes, vertical stripes, no stripes
# NUM OF STRIPES
#LOGO LOCATION, TOP LEFT, CENTER, TOP RIGHT
# LOGO TYPE (SUN, MOON, STAR, WHEAT, TREE)
if __name__ == "__main__":

    # Testing some hashes.
    hash1 = "0396233d5b28eded8e34c1bf9dc80fae34756743594b9e5ae67f4f7d124d2e3d"
    hash2 = "ef101b0bc42f41e23e325f3da71daeff43ff7df9d41ff268e53a06c767de8487"
    hash3 = "ca4da36c48be1c0b87a7d575c73f6e42"

    h1 = grind_hash_for_colors(hash1)
    h2 = grind_hash_for_colors(hash2)
    h3 = grind_hash_for_colors(hash3)

    test_pad = pad_hashcode("575758")
    #run above before grinds to ensure long enough hash to generate choices below
    
    h4 = grind_hash_for_stripe_style("5555556c48be1c0b87a7d575c73f6e42fnfhasdf341123abadbdbd")
    h5 = grind_hash_for_colors("5555556c48be1c0b87a7d575c73f6e42fnfhasdf341123abadbdbd")
    h6 = grind_hash_for_stripe_number("5555556c48be1c0b87a7d575c73f6e42fnfhasdf341123abadbdbd")
    h7 = grind_hash_for_symbol_locations("5555556c48be1c0b87a7d575c73f6e42fnfhasdf341123abadbdbd")
    h8 = grind_hash_for_symbol_number("5555556c48be1c0b87a7d575c73f6e42fnfhasdf341123abadbdbd")
    h9 = grind_hash_for_symbol_types("000010000100000010000000999999")
    #COULD SEND IN INPUT STRING REVERSED TO GENERATE SECOND HASH FOR SECOND SYMBOL PROPERTIES
    print(h4)
    print(h5)
    print(h6)
    print(h7)
    print(h8)
    print(h9)
    
    hex2rgb('#ffffff')
    hex2rgb('#ffff00')
    hex2rgb('#f5f5f5')