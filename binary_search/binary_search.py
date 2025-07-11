import random
import time
# Here we aim to prove that binary search is faster than naive search

# First let's create the function for naive search.
def naive_search(l, target):
    # example l: [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# if our list is sorted
# we can leverage that for binary search
def binary_search(l, target, low=None, high=None):
    # example l: [1, 3, 10, 12, 15]
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    
    midpoint = (high + low) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        return binary_search(l, target, midpoint+1, high)
    
if __name__ == "__main__":
    l = [1, 3, 5, 10, 12]
    target = 12
    print(naive_search(l, target))
    print(binary_search(l, target))