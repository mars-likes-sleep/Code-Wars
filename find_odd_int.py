"""
Given an array of integers, find the one that appears an odd number of 
times.

There will always be only one integer that appears an odd number of 
times.
"""

def find_it(seq):
    for integer in seq:
        if seq.count(integer) % 2 != 0:
            return integer
