# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def isPalindronePermutation(s):
        s = s.lower().replace(" ", "")
        size = len(s)
        dict = {}

        for i in range(size):
            dict[s[i]] = dict.get(s[i], 0) + 1

        exceptionFlag = False
        for val in dict.values():
            if val == 1:
                if not exceptionFlag:
                    exceptionFlag = True
                else:
                    return False
            elif val % 2 != 0:
                return False

        return True

print(isPalindronePermutation("Tact Coa"))
print(isPalindronePermutation("Tac Coa"))

#similar to checkPermutation, except its one string and we are allowed to have exactly one letter as the middle
#time complexity: O(n)