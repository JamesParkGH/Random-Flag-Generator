## @file TestHashGenerator.py
#  @title TestHashGenerator
#  @brief Tests implementation of HashGenerator for generating hexidecimal
#         hash digests from given input strings and hashing algorithms
#  @details Tests both public and private helper functions
#  @author Nathaniel Hu
#  @date 2022-02-25

import pytest
import hashlib

import HashGenerator


## @brief test cases for HashGenerator library module
class TestHashGenerator:
    # initialize
    def setup_method(self, method):
        self.hash_algos = {hash_algo: hashlib.new(hash_algo) for hash_algo in hashlib.algorithms_available}

    # reset
    def teardown_method(self, method):
        self.hash_algos = None

    # test _get_hash_algo() helper method (normal case)
    def test_get_hash_algo_0(self):
        assert HashGenerator._get_hash_algo('sha256') == self.hash_algos['sha256']

    # test _get_hash_hex() helper method (normal case)
    def test_get_hash_hex_0(self):
        assert HashGenerator._get_hash_hex('test', self.hash_algos['sha256']) == '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'

    # test hash_generator() method (normal case)
    def test_hash_generator_0(self):
        assert HashGenerator.hash_generator('sample') == 'af2bdbe1aa9b6ec1e2ade1d694f41fc71a831d0268e9891562113d8a62add1bf'

