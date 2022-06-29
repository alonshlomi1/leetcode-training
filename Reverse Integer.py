def reverse(x):
    newNum = 0
    flag =1
    if x < 0:
        flag =-1
        x *= -1
    while x > 0 :
        temp = x%10
        newNum *= 10
        newNum += temp
        x = int(x/10)
    if -pow(2,31) >= newNum*flag or newNum*flag >= (pow(2,31) - 1):
        return 0
    return newNum*flag



print(reverse(1534236469))