def lengthOfLastWord(s):
    CurrentLastWordLength = 0
    lastWordLength = 0
    i = 0
    for i in range(len(s)):
        if s[i].isalpha():
            CurrentLastWordLength += 1
            lastWordLength = CurrentLastWordLength
        if s[i] == ' ':
            CurrentLastWordLength = 0
    return lastWordLength


print(lengthOfLastWord(" s      "))


#V