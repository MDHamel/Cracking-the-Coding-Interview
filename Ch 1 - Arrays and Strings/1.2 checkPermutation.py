# Check Permutation: Given two strings, write a method to decide if one is a permutation of the
# other.

def checkPermutation(a, b):
    size = len(a)
    if size != len(b):
        return False

    dict = {}

    for i in range(size):
        dict[a[i]] = dict.get(a[i], 0) + 1
        dict[b[i]] = dict.get(b[i], 0) + 1

    for val in dict.values():
        if val % 2 != 0:
            return False

    return True

print(checkPermutation("asdf", "fdsa"))
print(checkPermutation("assf", "fdsa"))

# O(n)