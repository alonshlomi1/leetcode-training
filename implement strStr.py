def strStr(haystack, needle):
    lenNeedle = len(needle)
    for x in range(len(haystack)-lenNeedle+1):
        if (haystack[x:x + lenNeedle] == needle):
            return x
    return -1


print(strStr("mississippi","issi"))

#V