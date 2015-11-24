def check_permutation(str1, str2):
    """
    Given two strings, write a method to decide if one is a permutation of the other.
    (There is a solution in N log N time. Can you find one in N?)
    """
    hashmap = {}

    # sanity check
    if len(str1) != len(str2):
        return False

    # loop through first string and build up hashmap
    for character in str1:
        if character not in hashmap:
            hashmap[character] = 0
        hashmap[character] += 1

    # loop through str2 and check counts
    for character in str2:
        if character in hashmap:
            if hashmap[character] == 0:
                return False
            else:
                hashmap[character] -= 1
        else:
            return False
    return True

# tests

str1 = ''
str2 = ''
assert check_permutation(str1, str2)

str1 = 'abcabc'
str2 = 'abcabc'
assert check_permutation(str1, str2)

str1 = 'abcabc'
str2 = 'cbacba'
assert check_permutation(str1, str2)

str1 = 'abcabc'
str2 = 'aabbcc'
assert check_permutation(str1, str2)

str1 = 'abcabc'
str2 = ''
assert check_permutation(str1, str2) == False

str1 = ''
str2 = 'abcabc'
assert check_permutation(str1, str2) == False

str1 = 'abcabc'
str2 = 'aabbc'
assert check_permutation(str1, str2) == False

