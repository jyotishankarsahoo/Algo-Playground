"""Given an array, return true if there are two elements within a window of size 
k that are equal.
"""

def closeDuplicatesBruteForce(nums: list[int], k: int):
    for left in range(len(nums)):
        for right in range(left + 1, min(len(nums),left + k)):
            if nums[left] == nums[right]:
                return True
    return False

def closeDuplicatesSlidingWindow(nums: list[int], k: int):
    left = 0
    window = set()
    for right in range(len(nums)):
        if right - left + 1 > k:
            window.remove(nums[left])
            left += 1
        if nums[right] in window:
            return True
        window.add(nums[right])
    return False

print(f"Contains Duplicates in Range:{closeDuplicatesBruteForce([1,2,3,2,3,4], 2)}")
print(f"Contains Duplicates in Range:{closeDuplicatesSlidingWindow([1,2,3,2,3,4], 2)}")

"""Number of Sub Arrays of Size K and Avg Greater than or Equal to Threshold

You are given an array of integers arr and two integers k and threshold, 
return the number of sub-arrays of size k and average greater than or equal to threshold.

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4

Output: 3
"""