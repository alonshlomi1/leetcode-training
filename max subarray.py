def maxSubArray(nums):
    maxSubArray = nums[0]
    i=0
    j=1
    while j<= len(nums):
        if sum(nums[i:j]) > maxSubArray:
            maxSubArray = sum(nums[i:j])
        if sum(nums[i:j]) <= 0 and i<j-1:
            i+=1
        else:
            j+=1
    return maxSubArray

print(maxSubArray([-2,3,1,3]))

