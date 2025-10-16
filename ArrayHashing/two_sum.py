"""
Given an array of integers nums and an integer target, 
return the indices i and j such that nums[i] + nums[j] == target and i != j.
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
"""

def twoSumBrute(nums: list[int], target: int):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return []

def twoSumHashmap(nums: list[int], target: int):
    targetMap = {}
    for i in range(len(nums)):
        current_num = nums[i]
        complement = target - current_num
        if complement in targetMap:
            return [targetMap[complement], i]
        else:
            targetMap[current_num] = i
    return []
            
print(f"Two Sum: {twoSumBrute([3,4,5,6], 7)}")
print(f"Two Sum: {twoSumBrute([4,5,6], 11)}")
print(f"Two Sum: {twoSumBrute([5,5], 10)}")

print(f"Two Sum: {twoSumHashmap([5,5], 10)}")
print(f"Two Sum: {twoSumHashmap([4,5,6], 7)}")
print(f"Two Sum: {twoSumHashmap([3,4,5,6], 11)}")
