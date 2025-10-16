"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Return the 1-based indices of the two numbers as an array [index1, index2].
"""

def twoSumSortedArray(nums: list[int], target: int):
    left = 0
    right = len(nums) - 1
    while left < right:
        currentSum = nums[left] + nums[right]
        if currentSum == target:
            return [left, right]
        elif currentSum < target:
            left += 1
        else:
            right -= 1
    return []

print(f"Two Sum: {twoSumSortedArray([5,5], 10)}")
print(f"Two Sum: {twoSumSortedArray([4,5,6], 7)}")
print(f"Two Sum: {twoSumSortedArray([3,4,5,6], 11)}")