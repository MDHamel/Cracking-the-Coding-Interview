# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.


def oneAway(a, b):
    pair = [a,b]
    pair.sort(key=len)

    big = pair[1]
    small = pair[0]

    if (len(big) - len(small)) > 1:
        return False

    pivot = len(big)

    for i in range(len(small)):
        if big[i] != small[i]:
            pivot = i
            break

    bigPivotPlus1 = big[pivot+1:]
    smallPivotPlus1 = small[pivot+1:]

    # since we determined that the first half (before the pivot) is the same in both strings, we can ignore checking if
    # they are equal in this next step. we are merely checking if the change is a(n) 1) inserted char, 2)removed char,
    # or 3) an added char
    removalCheck = bigPivotPlus1 == small[pivot:]
    changedCheck = bigPivotPlus1 == smallPivotPlus1
    addedCheck = bigPivotPlus1 == smallPivotPlus1

    return removalCheck or changedCheck or addedCheck

# Time complexity: O(min(len(a), len(b)), or the minimum length between a and b being the bottleneck for this function


print(oneAway("pale", "ple"))
print(oneAway("pale", "pales"))
print(oneAway("pale", "bale"))
print(oneAway("bake", "pale"))



# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false