"""
Given an integer array nums, 
return true if any value appears more than once in the array, 
otherwise return false.
"""

def hasDuplicateSetLength(nums: list[int]) -> bool:
    unique_elements = set()
    for num in nums:
        unique_elements.add(num)
    return len(unique_elements) < len(nums)

def hasDuplicateSet(nums: list[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def hasDuplicateBrute(nums: list[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums [j]:
                return True
    return False


print(f"Has Duplicates: {hasDuplicateSetLength([1,2,3,5,3])}")
print(f"Has Duplicates: {hasDuplicateSetLength([1,2,3,4])}")
print(f"Has Duplicates: {hasDuplicateBrute([1,2,3,5,3])}")
print(f"Has Duplicates: {hasDuplicateBrute([1,2,3,4])}")
print(f"Has Duplicates: {hasDuplicateSet([1,2,3,5,3])}")
print(f"Has Duplicates: {hasDuplicateSet([1,2,3,4])}")