# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

def URLify(s):
    stringList = s.split(" ")
    return "%20".join(stringList)

# O(n) complexity when using string building techniques, concatting otherwise is O(n*k)
# where n is the length of the input string and k is the average length of the strings