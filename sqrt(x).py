def mySqrt(x):
    i=1
    while i*i <= x:
        i+=1
    return i-1


print(mySqrt(16))