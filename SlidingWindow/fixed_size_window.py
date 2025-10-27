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
def numOfSubArrays(arr: list[int], k: int, threshold: int) -> int:
    left = 0
    # Current Window Sum
    current_window_sum = 0
    # Result Count
    result_count = 0
    # Target Sum
    target_sum = k * threshold
    sub_array = []
    for right in range(len(arr)):
        current_window_sum += arr[right]
        # If current window size is exceeds the expected window size
        if right - left + 1 > k:
            # Reduce the total sum from left
            current_window_sum -= arr[left]
            # Increment the left pointer
            left += 1
        if right - left + 1 == k and current_window_sum >= target_sum:
            # Increment counter
            result_count += 1
            sub_array.append(arr[left:right+1])
    print(f"numOfSubArrays: Sub-arrays with average >= {threshold}: {sub_array}")
    return result_count

print(f"numOfSubArrays: {numOfSubArrays([2,2,2,2,5,5,5,8], 3, 4)}")

"""
Maximum Sum Sub-array of Size K:
    Problem: Given an array of integers and an integer k, 
        find the maximum sum of any contiguous sub-array of size k.
    Goal: Find the maximum window_sum.
    
Array (arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0], k =3)
"""

def maximumSumSubArray(arr: list[int], k: int):
    left = 0
    window_sum = 0
    max_sum = 0
    sub_array = []
    for right in range(len(arr)):
        window_sum += arr[right]
        if right - left + 1 > k:
            window_sum -= arr[left]
            left += 1
        if right - left + 1 == k and window_sum > max_sum:
            max_sum = window_sum
            sub_array = arr[left:right+1]
    print(f"maximumSumSubArray: Sub-array with maximum sum: {sub_array}")
    return max_sum

print(f"maximumSumSubArray: {maximumSumSubArray([4, 2, 1, 7, 8, 1, 2, 8, 1, 0], 3)}")

"""
Count Sub-arrays with Sum Less Than S:
    Problem: 
        Given an array of non-negative integers and two integers k and S, 
        return the number of sub-arrays of size exactly k whose 
        sum is strictly less than S.
    Goal: Count windows where window_sum < S.
"""
def subArraySumLessThanS(arr: list[int], k: int, s: int):
    left = 0
    window_sum = 0
    result_count = 0
    sub_array = []
    for right in range(len(arr)):
        window_sum += arr[right]
        if right - left + 1 > k:
            window_sum -= arr[left]
            left += 1
        if right - left + 1 == k and window_sum < s:
            result_count += 1
            sub_array.append(arr[left:right+1])
    print(f"subArraySumLessThanS: Sub-arrays with sum less than {s}: {sub_array}")
    return result_count

print(f"subArraySumLessThanS: {subArraySumLessThanS([1, 5, 2, 1, 4, 3, 2, 1], 4, 10)}")

"""
Maximum Number of Vowels in a Substring of Given Length:
    Problem: 
        Given a string s and an integer k, 
        find the maximum number of vowel letters ('a', 'e', 'i', 'o', 'u') 
        in any contiguous substring of length k.
    Goal: Track the count of vowels in the sliding window and find the max count.
"""

def maxVowelsSubstring(s: str, k: int):
    left = 0
    max_vowels = 0
    current_vowel_count = 0
    sub_string = ""
    vowels = {"a", "e", "i", "o", "u"}
    for right in range(len(s)):
        if s[right] in vowels:
            current_vowel_count += 1
        if right - left + 1 > k:
            if s[left] in vowels:
                current_vowel_count -= 1
            left += 1
        if right - left + 1 == k:
            if current_vowel_count >= max_vowels:
                max_vowels = current_vowel_count
                sub_string = s[left:right+1]
    return max_vowels, sub_string

print(f"maxVowelsSubstring: {maxVowelsSubstring('abciiidef', 3)}")


"""
Count Substrings with All Unique Characters:
    Problem: 
        Given a string S and an integer K, 
        count the number of contiguous substrings of length K 
        that contain exactly K unique characters (meaning all characters are unique).
    Goal: Use a frequency map/set inside the window to check if its size equals K 
        (or its count equals K).
    Sample Input: S = "havefunonleetcode", K = 5
    Sample Output: 6
    description: The substrings are "havef", "avefu", "vefun", "efuno", "etcod", "tcode".
"""

def countKUniqueCharSubstrings(s: str, k: int):
    left = 0
    num_of_subArray = 0
    sub_strings = []
    frequency_counter = {}
    for right in range(len(s)):
        if s[right] in frequency_counter:
            frequency_counter[s[right]] += 1
        else:
            frequency_counter[s[right]] = 1
        if right - left + 1 > k:
            frequency_counter[s[left]] -= 1
            if frequency_counter[s[left]] == 0:
                del frequency_counter[s[left]]
            left += 1
        if right - left + 1 == k and len(frequency_counter) == k:
            num_of_subArray += 1
            sub_strings.append(s[left: right + 1])
    print(f"countKUniqueCharSubstrings: substring: {sub_strings}")
    return num_of_subArray

print(f"countKUniqueCharSubstrings: {countKUniqueCharSubstrings("havefunonleetcode", 5)}")