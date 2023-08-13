# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def isUnique(s):
    for i in range(1, len(s)):
        if s[i] in s[:i-1]:
            return False
        return True
#complexity: O(n^2)

def isUniqueSorted(s):
    sorted_s = sorted(s)
    for i in range(1, len(sorted_s)):
        if sorted_s[i] == sorted_s[i - 1]:
            return False
    return True

#O(n log n) because the sort method is the bottle neck, then running through the list is O(n)