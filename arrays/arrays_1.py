def is_unique(collection):
    """
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?

    Args:
        collection (list)

    Returns:
        bool: True if collection contains all unique characters
    """
    # copy collection in order to not mutate original
    copy = collection[:]
    # sort collection, then check if adjacent collection elements are unique
    copy.sort()
    
    for i in range(len(copy)-1):
        if copy[i] == copy[i+1]:
            return False
    return True



# test cases
l1 = []
assert is_unique(l1) == True

l2 = ['c', 'b', 'a', 'A']
assert is_unique(l2) == True

# test unsorted duplicates
l3 = ['a', 'b', 'a', 'b', 'c', 'd']
assert is_unique(l3) == False
# check for mutation
assert l3 == ['a', 'b', 'a', 'b', 'c', 'd']

l4 = ['a', 'a', 'a']
assert is_unique(l4) == False