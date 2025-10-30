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

"""
Two Pointers (Opposite Ends) - Finding a Pair Sum
    Problem: 
        Two Sum II (Input Array Is Sorted)
        Goal: Given a sorted array of integers, numbers, 
            and a target sum, T, 
            find two numbers such that they add up to T. 
            Return the 1-based indices of the two numbers.
    Example:
        Input: numbers = [2,7,11,15], target = 9
        Output: [0,1]
"""

def twoSumSorted(arr: list[int], target: int):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        totalSum = arr[start] + arr[end]
        if totalSum == target:
            return (start, end)
        elif totalSum > target:
            end -= 1
        else:
            start += 1
    
print(f"twoSumSorted: {twoSumSorted([2,7,11,15], 9)}")

        
"""
Two Pointers (Same Direction) - Removing Duplicates In-Place
    Problem: 
        Remove Duplicates from Sorted Array
    Goal: 
        Given a sorted array of integers, 
        remove the duplicates in-place such that 
        each unique element appears only once. 
        Return the length of the new array (the number of unique elements). 
        The elements beyond the returned length do not matter.
    Example:
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4]
"""

def removeDuplicateFromSortedArray(arr: list[int]):
    slow = 1
    fast = 1
    while fast < len(arr):
        if arr[fast] != arr[fast - 1]:
            arr[slow] = arr[fast]
            slow += 1
        fast += 1
    print(f"Modified Array (Unique Part): {arr[:slow]}")
    return slow  
    
print(f"removeDuplicateFromSortedArray: {removeDuplicateFromSortedArray([0,0,1,1,1,2,2,3,3,4])}")
        