# @file TestHashToFlag.py
#  @title TestHashToFlag
#  @brief Tests implementation of the HashToFlag
#         library helper functions.
#  @author Akram Hannoufa
#  @date 2022-03-16

from pytest import *
import HashToFlag


# @brief test cases for HashToFlag library module
class TestHashToFlag:
    # initialize
    def setup_method(self, method):
        self.string1 = "abcdeabcdeabcdeabcdeabcdeabcde"
        self.string2 = ("abcdeabcdeabcdeabcdeabcdeabcdeabcdea"
                        "bcdeabcdeabcdeabcdeabcde")
        self.string3 = "123456789012265622412254892829428"
        self.string4 = "ffffefefefefefefefefefe"
        self.string5 = "11111111111111111111111111111111111111"
        self.string6 = ""

    # reset
    def teardown_method(self, method):
        self.string1 = None
        self.string2 = None
        self.string3 = None
        self.string4 = None
        self.string5 = None
        self.string6 = None

    # test grind_hash_for_colors (correctness)
    def test_grind_hash_for_colors_0(self):
        assert HashToFlag.grind_hash_for_colors(self.string1) == [(
            171, 205, 234), (188, 222, 171),
            (205, 234, 188), (222, 171, 205), (234, 188, 222)]

    # test grind_hash_for_colors (correctness)
    def test_grind_hash_for_colors_1(self):
        assert HashToFlag.grind_hash_for_colors(self.string2) == [(
            171, 205, 234), (188, 222, 171),
            (205, 234, 188), (222, 171, 205), (234, 188, 222)]

    # test grind_hash_for_colors (correctness)
    def test_grind_hash_for_colors_2(self):
        assert HashToFlag.grind_hash_for_colors(
            self.string2) == HashToFlag.grind_hash_for_colors(self.string1)

    # test grind_hash_for_colors
    # (blank hashcode gives error -- no decision possible)
    def test_grind_hash_for_colors_3(self):
        with raises(IndexError):
            HashToFlag.grind_hash_for_colors(self.string6)

    # test grind_hash_for_stripe_style (correctness)
    def test_grind_hash_for_stripe_style_0(self):
        assert HashToFlag.grind_hash_for_base_stripe_style(
            self.string1) == "SALTIRE"

    # test grind_hash_for_stripe_style (correctness)
    def test_grind_hash_for_stripe_style_1(self):
        assert HashToFlag.grind_hash_for_base_stripe_style(
            self.string3) == "NONE"

    # test grind_hash_for_stripe_style (correctness)
    def test_grind_hash_for_stripe_style_2(self):
        assert HashToFlag.grind_hash_for_base_stripe_style(
            self.string1) == (
            HashToFlag.grind_hash_for_base_stripe_style(self.string2))

    # test grind_hash_for_stripe_style
    # (blank hashcode gives error -- no decision possible)
    def test_grind_hash_for_stripe_style_3(self):
        with raises(ValueError):
            HashToFlag.grind_hash_for_base_stripe_style(self.string6)

    # test grind_hash_for_stripe_number (correctness)
    def test_grind_hash_for_stripe_number_0(self):
        assert HashToFlag.grind_hash_for_stripe_number(
            self.string1) == (
            HashToFlag.grind_hash_for_stripe_number(self.string2))

    # test grind_hash_for_stripe_number (correctness)
    def test_grind_hash_for_stripe_number_1(self):
        assert HashToFlag.grind_hash_for_stripe_number(self.string1) == "SIX"

    # test grind_hash_for_stripe_number (correctness)
    def test_grind_hash_for_stripe_number_2(self):
        assert HashToFlag.grind_hash_for_stripe_number(self.string3) == (
                                                                         "THR"
                                                                         "EE")

    # test grind_hash_for_stripe_number (correctness)
    def test_grind_hash_for_stripe_number_3(self):
        assert HashToFlag.grind_hash_for_stripe_number(
            self.string4) == "TWELVE"

    # test grind_hash_for_stripe_number
    # (blank hashcode gives error -- no decision possible)
    def test_grind_hash_for_stripe_number_4(self):
        with raises(ValueError):
            HashToFlag.grind_hash_for_stripe_number(self.string6)

    # test grind_hash_for_symbol_location (correctness)
    def test_grind_hash_for_symbol_location_0(self):
        assert HashToFlag.grind_hash_for_symbol_locations(
            self.string1) == (
            HashToFlag.grind_hash_for_symbol_locations
            (self.string2))

    # test grind_hash_for_symbol_location (correctness)
    def test_grind_hash_for_symbol_location_1(self):
        assert HashToFlag.grind_hash_for_symbol_locations(
            self.string1) == "TOP_RIGHT"

    # test grind_hash_for_symbol_location (correctness)
    def test_grind_hash_for_symbol_location_2(self):
        assert HashToFlag.grind_hash_for_symbol_locations(
            self.string3) == "TOP_LEFT"

    # test grind_hash_for_symbol_location
    # (blank hashcode gives error -- no decision possible)
    def test_grind_hash_for_symbol_location_3(self):
        with raises(ValueError):
            HashToFlag.grind_hash_for_symbol_locations(self.string6)

    # test grind_hash_for_symbol_number (correctness)
    def test_grind_hash_for_symbol_number_0(self):
        assert HashToFlag.grind_hash_for_symbol_number(
            self.string1) == (
                        HashToFlag.grind_hash_for_symbol_number(self.string2))

    # test grind_hash_for_symbol_number (correctness)
    def test_grind_hash_for_symbol_number_1(self):
        assert HashToFlag.grind_hash_for_symbol_number(self.string1) == "TWO"

    # test grind_hash_for_symbol_number (correctness)
    def test_grind_hash_for_symbol_number_2(self):
        assert HashToFlag.grind_hash_for_symbol_number(self.string3) == "ONE"

    # test grind_hash_for_symbol_number
    # (blank hashcode gives error -- no decision possible)
    def test_grind_hash_for_symbol_number_3(self):
        with raises(ValueError):
            HashToFlag.grind_hash_for_symbol_number(self.string6)

    # test grind_hash_for_symbol_types (correctness)
    def test_grind_hash_for_symbol_types_0(self):
        assert HashToFlag.grind_hash_for_symbol_types(
            self.string1) == (
            HashToFlag.grind_hash_for_symbol_types(self.string2))

    # test grind_hash_for_symbol_types (correctness)
    def test_grind_hash_for_symbol_types_1(self):
        assert HashToFlag.grind_hash_for_symbol_types(self.string1) == "SWORD"

    # test grind_hash_for_symbol_types (correctness)
    def test_grind_hash_for_symbol_types_2(self):
        assert HashToFlag.grind_hash_for_symbol_types(
            self.string3) == "ROUNDEL"

    # test grind_hash_for_symbol_types (correctness)
    def test_grind_hash_for_symbol_types_3(self):
        assert HashToFlag.grind_hash_for_symbol_types(self.string5) == "NONE"

    # test grind_hash_for_symbol_types
    # (blank hashcode gives error -- no decision possible)
    def test_grind_hash_for_symbol_types_4(self):
        with raises(ValueError):
            HashToFlag.grind_hash_for_symbol_types(self.string6)

    # test grind_hash_for_base_stripe_style (correctness)
    def test_grind_hash_for_base_stripe_style_0(self):
        assert HashToFlag.grind_hash_for_base_stripe_style(
            self.string1) == (
            HashToFlag.grind_hash_for_base_stripe_style(self.string2))

    # test grind_hash_for_base_stripe_style (correctness)
    def test_grind_hash_for_base_stripe_style_1(self):
        assert HashToFlag.grind_hash_for_base_stripe_style(
            self.string1) == "SALTIRE"

    # test grind_hash_for_base_stripe_style (correctness, None)
    def test_grind_hash_for_base_stripe_style_2(self):
        assert HashToFlag.grind_hash_for_base_stripe_style(
            self.string3) == "NONE"

    # test grind_hash_for_base_stripe_style
    # (blank hashcode gives error -- no decision possible)
    def test_grind_hash_for_base_stripe_style_3(self):
        with raises(ValueError):
            HashToFlag.grind_hash_for_base_stripe_style(self.string6)

    # test grind_hash_for_overlay_stripe_style (correctness)
    def test_grind_hash_for_overlay_stripe_style_0(self):
        assert HashToFlag.grind_hash_for_overlay_stripe_style(
            self.string1) == (
            HashToFlag.grind_hash_for_overlay_stripe_style(self.string2))

    # test grind_hash_for_overlay_stripe_style (correctness)
    def test_grind_hash_for_overlay_stripe_style_1(self):
        assert HashToFlag.grind_hash_for_overlay_stripe_style(
            self.string1) == "SALTIRE_THIN"

    # test grind_hash_for_overlay_stripe_style (correctness, None)
    def test_grind_hash_for_overlay_stripe_style_2(self):
        assert HashToFlag.grind_hash_for_overlay_stripe_style(
            self.string3) == "NONE"

    # test grind_hash_for_overlay_stripe_style
    # (blank hashcode gives error -- no decision possible)
    def test_grind_hash_for_overlay_stripe_style_3(self):
        with raises(ValueError):
            HashToFlag.grind_hash_for_overlay_stripe_style(self.string6)
