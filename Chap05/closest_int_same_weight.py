from test_framework import generic_test

'''
Define the weight of a nonnegative integer x to be the number of bits that are set to
1 in its binary representation. For example, since 92 in base-2 equals (1011100)2, the
weight of 92 is 4.
Write a program which takes as input a nonnegative integer x and returns a number
y which is not equal to x, but has the same weight as x and their difference, |y- x|, is
as small as possible. You can assume x is not 0, or all Is. For example, if x = 6, you
should return 5.
'''

def closest_int_same_bit_count(x: int) -> int:
    # TODO - you fill in here.
    for i in range (63):
        if (x >> i) & 1 != (x >> (i+1)) & 1:
            x ^= (1 << i) | (1 << (i+1))
            return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
