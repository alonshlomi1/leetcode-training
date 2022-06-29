def singleNumber(nums):
    if len(nums)==1:
        return nums[0]
    i=0
    nums= sorted(nums)
    while i<len(nums):
        if i<len(nums)-1 and nums[i] == nums[i+1]:
            i+=2
        else:
            return nums[i]



print(singleNumber([2]))