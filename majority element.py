def majorityElement(nums):
    i=0
    dict = {}
    while i< len(nums):
        if nums[i] in dict:
            dict[nums[i]] = dict[nums[i]]+1
        else:
            dict[nums[i]] = 1
        i+=1
    return max(dict, key=dict.get)


print(majorityElement([1,1,1,2,2,2,2,22,222,22,2,1,1,1,1,1,2,2,2,2]))