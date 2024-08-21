## @file HashGenerator.py
#  @title HashGenerator
#  @brief A library module for getting the hexidecimal hash of a given string
#  @details HashGenerator module, uses no other modules; no exported constants
#           or types, no state or environment variables, no state invariant
#           or assumptions
#  @author Nathaniel Hu
#  @date 2022-03-31

import hashlib
import sys


## @brief gets the hashing algorithm from the dictionary of available hashing
#         algorithms using the given input hash type string
#  @details the default hashing algorithm, SHA-256, is used if the input hash
#           type is not in the dictionary of available hashing algorithms
#  @param hash_type a string representing the selected hashing algorithm
#  @return selected hashing algorithm if found; otherwise SHA-256 hashing
#          algorithm returned
def _get_hash_algo(hash_type):
    # @var hash_algos
    #  the dictionary of all hashing algorithms available on this local machine
    hash_algos = {hash_algo: hashlib.new(hash_algo)
                  for hash_algo in hashlib.algorithms_available}
    if hash_type in hash_algos:
        return hash_algos[hash_type]
    return hash_algos['sha256']


## @brief gets the hexidecimal representation of the hashing digest using the
#         given input string and hashing algorithm
#  @details the byte encoding will be specified per the Python version used
#  @param hash_input a string that will be run through the given hashing
#                    algorithm to get a hexidecimal hashing digest
#  @param hash_algo a hashing algorithm that will be used to turn the input
#                   string into a hexidecimal hashing digest
#  @return hexidecimal hashing digest obtained from the given input string
#          using the given hashing algorithm
def _get_hash_hex(hash_input, hash_algo):
    hash_input_bytes = bytes()
    # specifies byte encoding depending on
    # python version (2 or 3; may remove later?)
    if sys.version_info.major == 2:
        hash_input_bytes = bytes(hash_input)
    else:
        hash_input_bytes = bytes(hash_input, 'utf-8')

    hash_algo.update(hash_input_bytes)
    try:
        return hash_algo.hexdigest()
    # included to specify hash digest length for shake hashing algorithms
    except TypeError:
        return hash_algo.hexdigest(32)


## @brief generates a hashing digest using the given input string and hashing
#         algorithm
#  @details the hashing algorithm SHA-256 will be used by default if none is
#           specified
#  @param hash_input a string that will be run through the given hashing
#                    algorithm to get a hexidecimal hashing digest
#  @param hash_type a string representing the selected hashing algorithm
#  @return hexidecimal hashing digest obtained from the given input string
#          using the given hashing algorithm
def hash_generator(hash_input, hash_type='sha256'):
    # @var hash_algo
    #  the hashing algorithm to be used to generate the hash digest from the
    #  given input string
    hash_algo = _get_hash_algo(hash_type)
    return _get_hash_hex(hash_input, hash_algo)
