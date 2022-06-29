def isPalindrome(s):
    i = 0
    j = len(s)-1
    while i < j:
        if (s[i].isalpha() or s[i].isnumeric()) and (s[j].isalpha() or s[j].isnumeric()):
            if s[i].lower() != s[j].lower():
                return False
            j -= 1
            i += 1
        else:
            if s[i].isalpha() or s[i].isnumeric():
                j-=1
            else:
                i+=1
    return True


print(isPalindrome("0P"))