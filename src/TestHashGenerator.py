## @file TestHashGenerator.py
#  @title TestHashGenerator
#  @brief Tests implementation of HashGenerator for generating hexidecimal
#         hash digests from given input strings and hashing algorithms
#  @details Tests both public and private helper functions
#  @author Nathaniel Hu
#  @date 2022-04-07

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

    # test _get_hash_algo() helper method (normal case, for correctness)
    def test_get_hash_algo_0(self):
        assert 'sha256' not in hashlib.algorithms_available or \
        HashGenerator._get_hash_algo('sha256').name == self.hash_algos['sha256'].name
        

    # test _get_hash_algo() helper method (normal case, for correctness)
    def test_get_hash_algo_1(self):
        assert 'sha256' not in hashlib.algorithms_available or \
        HashGenerator._get_hash_algo('sha512').name == self.hash_algos['sha512'].name
        

    # test _get_hash_algo() helper method (normal case, for correctness)
    def test_get_hash_algo_2(self):
        assert 'sha384' not in hashlib.algorithms_available or \
        HashGenerator._get_hash_algo('sha384').name == self.hash_algos['sha384'].name

    # test _get_hash_algot() helper method (exceptional case, for robustness)
    # 'sha128' is not an real hashing algorithm, thus helper method should default to 'sha256'
    def test_get_hash_algo_3(self):
        assert HashGenerator._get_hash_algo('sha128').name == self.hash_algos['sha256'].name and \
        'sha128' not in hashlib.algorithms_available
        

    # test _get_hash_algo() helper method (exceptional case, for robustness)
    # 'shake_512' is not an real hashing algorithm, thus helper method should default to 'sha256'
    def test_get_hash_algo_4(self):
        assert HashGenerator._get_hash_algo('shake_512').name == self.hash_algos['sha256'].name and \
        'shake_512' not in hashlib.algorithms_available

    # test _get_hash_hex() helper method (normal case, for correctness)
    def test_get_hash_hex_0(self):
        assert 'sha256' not in hashlib.algorithms_available or \
        HashGenerator._get_hash_hex('test', self.hash_algos['sha256']) == \
        '9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08'

    # test _get_hash_hex() helper method (normal case, for correctness)
    def test_get_hash_hex_1(self):
        assert 'md5' not in hashlib.algorithms_available or \
        HashGenerator._get_hash_hex('hello world', self.hash_algos['md5']) == \
        '5eb63bbbe01eeed093cb22bb8f5acdc3'

    # test _get_hash_hex() helper method (boundary/exception case, for correctness and robustness)
    # should initially fail because length of hash digest returned by this hashing algorithm
    # must be specified
    def test_get_hash_hex_2(self):
        assert 'shake_256' not in hashlib.algorithms_available or \
        HashGenerator._get_hash_hex('#S0m3R4nd0mStr!ng$*&(St@ff)', self.hash_algos['shake_256']) == \
        '84f67f46eaee40ff51d92a42c7f63508d5d8c27294e5243e6d2be3b38f1c3a1c'

    # test hash_generator() method (normal case, for correctness)
    def test_hash_generator_0(self):
        assert HashGenerator.hash_generator('sample') == \
        'af2bdbe1aa9b6ec1e2ade1d694f41fc71a831d0268e9891562113d8a62add1bf'

    # test hash_generator() method (normal case, for correctness)
    def test_hash_generator_1(self):
        assert 'md5' not in hashlib.algorithms_available or \
        HashGenerator.hash_generator('#HashItUp!', 'md5') == \
        'fef277df4020c9db33b9e1c5578c8b3b'

    # test hash_generator() method (boundary/exception case, for correctness and robustness)
    # should initially fail because length of hash digest returned by this hashing algorithm
    # must be specified
    def test_hash_generator_2(self):
        assert 'shake_128' not in hashlib.algorithms_available or \
        HashGenerator.hash_generator('$4mpl3T3$t!ng%', 'shake_128') == \
        'd4ac7a4d3359010eeb5afe76560bc8e33238f50f330aed12d6d171b5ab2257a8'

