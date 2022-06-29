def lengthOfLongestSubstring(s):
    longestStr = ''
    currentStr = ''
    for x in range(len(s)):
        if currentStr.__contains__(s[x]):
            currentStr = currentStr[currentStr.index(s[x])+1:len(currentStr)] + s[x]
        else:
            currentStr += s[x]
            if len(currentStr) > len(longestStr):
                longestStr = currentStr
    return len(longestStr)


a = 'abcabcbb'
b= 'bbbbb'
c = 'pwwkew'
d = ''
e = 'asdfgalkj'
print(lengthOfLongestSubstring(a))
print(lengthOfLongestSubstring(b))
print(lengthOfLongestSubstring(c))
print(lengthOfLongestSubstring(d))
print(lengthOfLongestSubstring(e))