import math
def titleToNumber(columnTitle):
    if len(columnTitle)==1:
        return ord(columnTitle[0]) - 64
    number = 0
    i = 0
    while i < len(columnTitle):
        number += (ord(columnTitle[len(columnTitle) - 1 - i]) - 64) * math.pow(26, i)
        i +=1
    return int(number)


print(titleToNumber("AC"))