# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompression(s):
    strings = []

    lastChar = s[0]
    count = 1

    for char in s[1:]:
        if char == lastChar:
            count += 1
        else:
            strings.append(lastChar)
            strings.append(str(count))
            count = 1
            lastChar = char

    #finish up the last char

    strings.append(lastChar)
    strings.append(str(count))

    return "".join(strings)



#time complexity: O(n)

print(stringCompression("aabcccccaaa"))
print(stringCompression("aabcccccaaaff"))
print(stringCompression("aabcccccaaaf"))
print(stringCompression("abc"))
print(stringCompression("a"))




# aabcccccaaa => a2blc5a3