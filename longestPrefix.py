def longestCommonPrefix(strs):
    sortestStrLen = len(sorted(strs,key=len)[0])
    curentPrefix = ''
    for x in range(sortestStrLen):
        curentletter = strs[0][x]
        for y in range(1,len(strs)):
            if strs[y][x] != curentletter:
                return curentPrefix
        curentPrefix += curentletter
    return curentPrefix


print(longestCommonPrefix(["flower","flow","flight"]))


VVVVV