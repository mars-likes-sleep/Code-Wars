#Optimal solution; couldn't figure this one out on my own

def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)

l1 = [2, 4, 3, 5, 8, 1, 6]

print(sum_pairs(l1, 9))
