import math
def isPalindrome(x):
    if len(x.__str__()) == 1:
        return True
    original = x
    backNum = 0
    i = pow(10, len(x.__str__())-1)
    while x > 0:
        backNum += i * (x % 10)
        x = int(x/10)
        i = int(i/10)
    if backNum == original:
        return True
    return False


print(isPalindrome(10))


VVVVV