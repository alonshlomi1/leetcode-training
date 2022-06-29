from builtins import sorted


def twoSum(nums, target):
    i=0
    j=(len(nums)-1)
    while i<j:
        if nums[i] +nums[j] == target:
            return [i,j]
        elif nums[i] +nums[j] > target:
            j-=1
        else:
            i+=1


print(twoSum([3,2,4],6))