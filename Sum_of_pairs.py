"""
Given a list of integers and a single sum value, return the first two
values (parse from the left please) in order of appearance that add up
to form the sum.
"""

#Optimal solution; couldn't initially figure this one out on my own.

def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
