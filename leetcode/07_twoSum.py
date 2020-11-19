def twoSum(nums: [int], target: int):
#   nums = []
#   target = int()

    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target-num in nums_map and i!=nums_map[target-num]:
            return nums.index(num), nums_map[target-num]

print(twoSum([2,7, 11, 15], 9))
