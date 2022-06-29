def searchInsert(nums, target):
    preIndex = len(nums)
    index = int(len(nums) / 2)
    while True:
        if (index + preIndex) / 2 in [index, index+1, index-1]:
            return index
        if nums[index] == target:
            return index
        elif
