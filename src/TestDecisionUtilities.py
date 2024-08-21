## @file TestDecisionUtilities.py
#  @title TestDecisionUtilities
#  @brief Tests implementation of the DecisionUtilities 
#         library helper functions.
#  @author Akram Hannoufa
#  @date 2022-03-17

from pytest import *
import DecisionUtilities


## @brief test cases for DecisionUtilities library module
class TestDecisionUtilities:
    # initialize
    def setup_method(self, method):
        self.string1 = "four"
        self.string2 = "much longer string so it does not need to be padded lol"

        self.list1 = [1,2,3,4]
        self.list2 = [1,2,3]

        self.pos1 = 6
        self.pos2 = 10.5

        self.neg1 = -8
        self.neg2 = -6.5

    # reset
    def teardown_method(self, method):
        self.string1 = None
        self.string2 = None

        self.list1 = None
        self.list2 = None

        self.pos1 = None
        self.pos2 = None
        
        self.neg1 = None
        self.neg2 = None

    # test pad_hashcode (short string)
    def test_pad_hashcode_0(self):
        assert len(DecisionUtilities.pad_hashcode(self.string1)) == 30

    # test pad_hashcode (short string)
    def test_pad_hashcode_1(self):
        assert len(DecisionUtilities.pad_hashcode(self.string1)) != len(self.string1)

    # test pad_hashcode (long enough string)
    def test_pad_hashcode_2(self):
        assert len(DecisionUtilities.pad_hashcode(self.string2)) == len(self.string2)

    # test pad_hashcode (long enough string)
    def test_pad_hashcode_3(self):
        assert len(DecisionUtilities.pad_hashcode(self.string2)) != 30
    
    # test pad_hashcode (type error)
    def test_pad_hashcode_4(self):
        with raises(TypeError):
            DecisionUtilities.pad_hashcode(36)

    # test pad_hashcode (type error)
    def test_pad_hashcode_5(self):
        with raises(TypeError):
            DecisionUtilities.pad_hashcode(True)

    # test choose_from_list (getting right item)
    def test_choose_from_list_0(self):
        assert DecisionUtilities.choose_from_list(self.list1, 2.4) == 3

    # test choose_from_list (getting right item)
    def test_choose_from_list_1(self):
        assert DecisionUtilities.choose_from_list(self.list1, 2.0) == 2

    # test choose_from_list (getting right item)
    def test_choose_from_list_2(self):
        assert DecisionUtilities.choose_from_list(self.list2, 2.0) == 2

    # test choose_from_list (value error)
    def test_choose_from_list_3(self):
        with raises(ValueError):
            DecisionUtilities.choose_from_list(self.list2, -7.5)

    # test choose_from_list (value error)
    def test_choose_from_list_4(self):
        with raises(ValueError):
            DecisionUtilities.choose_from_list(self.list2, -1)
 
    # test map_decision (generating correct index)
    def test_map_decision_0(self):
        assert approx(DecisionUtilities.map_decision(100,10,50),0.0001)== 5.04950495

    # test map_decision (generating correct index)
    def test_map_decision_1(self):
        assert DecisionUtilities.map_decision(0,0,0)  == 0

    # test map_decision (generating correct index)
    def test_map_decision_2(self):
        assert approx(DecisionUtilities.map_decision(50.5,11,10.5),0.001) == 2.4563106796

    # test map_decision (generating correct index)
    def test_map_decision_3(self):
        assert approx(DecisionUtilities.map_decision(0.05,2,10.5),0.001) == 21.904761
    
    # test map_decision (value error)
    def test_map_decision_4(self):
        with raises(ValueError):
            DecisionUtilities.map_decision(-0.05,2,10.5) 

    # test map_decision (value error)
    def test_map_decision_5(self):
        with raises(ValueError):
            DecisionUtilities.map_decision(0.05,-2,10.5) 

    # test map_decision (value error)
    def test_map_decision_6(self):
        with raises(ValueError):
            DecisionUtilities.map_decision(0.05,2,-10.5) 

    # test split_sequence (generating correct length lists)
    def test_split_sequence_0(self):
        assert len(DecisionUtilities.split_sequence(self.string2,5)) == 11

    # test split_sequence (generating correct length lists)
    def test_split_sequence_1(self):
        assert len(DecisionUtilities.split_sequence(self.string2,11)) == 5

    # test split_sequence (generating correct items)
    def test_split_sequence_2(self):
        assert (DecisionUtilities.split_sequence(self.string2,11))[0] == "much longer"

    # test split_sequence (generating correct items)
    def test_split_sequence_3(self):
        assert (DecisionUtilities.split_sequence(self.string2,5))[0] == "much "

    # test split_sequence (generating correct items)
    def test_split_sequence_4(self):
        assert (DecisionUtilities.split_sequence(self.string1,3))[1] == "r"

    # test split_sequence (generating correct items)
    def test_split_sequence_5(self):
        assert (DecisionUtilities.split_sequence(self.string1,3))[0] == "fou"
    
    # test split_sequence (generating correct items)
    def test_split_sequence_6(self):
        assert (DecisionUtilities.split_sequence(self.string2,11))[-1] == " padded lol"
    
    # test hex2rgb (generating correct rgb values)
    def test_hex2rgb_0(self):
        assert DecisionUtilities.hex2rgb("abcdef") == (171, 205, 239)
    
    # test hex2rgb (string wrong length)
    def test_hex2rgb_1(self):
        assert DecisionUtilities.hex2rgb("abcdef3232312knhmgf") == 0

    # test hex2rgb (generating correct rgb values)
    def test_hex2rgb_2(self):
        assert DecisionUtilities.hex2rgb("123456") == (18,52,86)

    # test hex2rgb (type error)
    def test_hex2rgb_3(self):
        with raises(TypeError):
            DecisionUtilities.hex2rgb(123456)

    # test diff (correctness)
    def test_diff_0(self):
        assert DecisionUtilities.diff(self.pos1,self.pos2) == 4

    # test diff (correctness)
    def test_diff_1(self):
        assert DecisionUtilities.diff(self.pos1,self.neg1) == 14
    
    # test diff (correctness)
    def test_diff_2(self):
        assert DecisionUtilities.diff(self.neg1,self.neg2) == 1
    
    # test diff (correctness)
    def test_diff_3(self):
        assert DecisionUtilities.diff(0,self.pos1) == 6