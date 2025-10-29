"""
Shortest SubArray with Sum Greater than or Equal to S
    Array [2, 1, 5, 2, 3, 2]
    Target Sum 7
    Output = 2 , [5,7]
"""

def shortestSubArraySum(arr: list[int], target: int):
    left = 0
    current_window_sum = 0
    min_length = float("inf")
    for right in range(len(arr)):
        # 1. EXPAND the window and update the sum
        current_window_sum += arr[right]
        # 2. CONTRACT the window WHILE the condition is met (window_sum >= S)
        while current_window_sum > target:
            min_length = min(min_length, right - left + 1)
            current_window_sum -= arr[left]
            left += 1
            
    return min_length

print(f"shortestSubArraySum: {shortestSubArraySum([2, 1, 5, 2, 3, 2], 7)}")
        
"""
Problem: 
    Given a string, S, and an integer, K, 
    find the length of the longest contiguous substring that contains 
    at most K distinct characters.
Goal: 
    Find max(right - left + 1) such that count(unique characters in window) <= K.
    
    s = araaci
    k = 2
    output = 4
""" 

def longestSubstringWithKDistinct(s: str, k: int):
    left = 0
    max_length = 0
    frq_map = {}
    start_index, end_index = 0, 0
    for right in range(len(s)):
        # Expand
        if s[right] in frq_map:
            frq_map[s[right]] += 1
        else:
            frq_map[s[right]] = 1
        # Contract
        while len(frq_map) > k:
            frq_map[s[left]] -= 1
            if frq_map[s[left]] == 0:
                del frq_map[s[left]]
            left += 1
        # max_length = max(max_length, right - left + 1)
        if right - left + 1 > max_length:
             max_length = right - left + 1
             start_index = left
             end_index = right
    print(s[start_index: end_index + 1])
             
    return max_length
print(f"longestSubstringWithKDistinct: {longestSubstringWithKDistinct("araaci", 5)}")

"""
Counting Subarrays with Product Less Than P
    Problem: 
        Given an array of positive integers, array, and a positive integer, P
        find the total number of contiguous subarrays 
        whose product is strictly less than P.
    Goal: Count all subarrays where window_product} < P.
    
    input: arr = [10, 5, 2, 6], P = 100
    output: 8
"""

def numberOfSubArraysWithProductLessThanP(arr: list[int], p: int):
    left = 0
    window_product = 1
    result_count = 0
    for right in range(len(arr)):
        window_product *= arr[right]
        while window_product >= p:
            window_product = window_product / arr[left]
            left +=1
        result_count += right - left + 1
    return result_count

print(f"numberOfSubArraysWithProductLessThanP: {numberOfSubArraysWithProductLessThanP([10, 5, 2, 6], 100)}")


"""
Longest Subarray with Ones After Replacement (Simplified)
    Problem: 
        Given a binary array (arr containing only 0s and 1s) and an integer, 
        M(the maximum number of 0s allowed), 
        find the length of the longest contiguous subarray containing at most M zeros.
    Goal: Find max(right - left + 1) such that count(0s in window) <= M.
    
    input: arr = [1,1,0,0,1,1,1,0,1,1], M = 2
    output: 7
"""

def lengthOfLongestSubArrayWithMostMZeros(arr: list[int], m: int):
    left = 0
    maxLength = 0
    numberOfZeros = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            numberOfZeros += 1
        
        while numberOfZeros > m:
            if arr[left] == 0:
                numberOfZeros -= 1
            left += 1
        
        currentLength = right - left + 1
        maxLength = max(maxLength, currentLength)
    return maxLength

print(f"lengthOfLongestSubArrayWithMostMZeros: {lengthOfLongestSubArrayWithMostMZeros([1,1,0,0,1,1,1,0,1,1], 2)}")

"""
Longest Substring Without Repeating Characters
    Problem: 
        Given a string, S, 
        find the length of the longest contiguous substring 
        that contains no repeating characters.
    Goal: Find max(right - left + 1) such that count(any character in window) <= 1.
    input: s = "abcabcbb"
    output: 3
"""
def longestSubstringWithoutRepeatingChar(s: str):
    max_length = 0
    left = 0
    freq_map = {}
    for right in range(len(s)):
        if s[right] in freq_map:
            freq_map[s[right]] += 1
        else:
            freq_map[s[right]] = 1
        while freq_map[s[right]] > 1:
            freq_map[s[left]] -= 1
            if freq_map[s[left]] == 0:
                del freq_map[s[left]]
            left += 1
        current_length = right - left + 1
        max_length = max(max_length, current_length)
    return max_length
print(f"longestSubstringWithoutRepeatingChar: {longestSubstringWithoutRepeatingChar("abcabcbb")}")

"""
Longest Substring with At Most Two Distinct Characters (Specific K)
    Problem: 
        Given a string, S, 
        find the length of the longest contiguous substring 
        that contains at most two distinct characters.
    Input: s = "eceba"
    Output: 3
    Explanation: The substring is "ece" which its length is 3.
"""

def longestSubstringWithAtAMostTwoDistinctChars(s: str):
    left = 0
    longestSubstringLength = 0
    frqMap = {}
    for right in range(len(s)):
        if s[right] in frqMap:
            frqMap[s[right]] += 1
        else:
            frqMap[s[right]] = 1
        while len(frqMap) > 2:
            frqMap[s[left]] -= 1
            if frqMap[s[left]] == 0:
                del frqMap[s[left]]
            left += 1
        currentSubStringLength = right - left + 1
        longestSubstringLength = max(currentSubStringLength, longestSubstringLength)
    return longestSubstringLength

print(f"longestSubstringWithAtAMostTwoDistinctChars: {longestSubstringWithAtAMostTwoDistinctChars("abcabcbb")}")


"""
Minimum Window Sort SubArray (Simplified for Window)
    Problem: 
        Given an array of integers, arr and an integer D, 
        find the length of the shortest contiguous subArray 
        whose sum is strictly less than D. Return 0 if no such subArray exists.
    input: arr = [2, 1, 5, 2, 3, 2], D = 7
    output: 1
    Explanation: The subArray [5, 2] has the minimum length under the problem
"""
def minWindowSubArraySumLessThanD(arr: list[int], d: int):
    left = 0
    minSubArrayLength = float("inf")
    subArraySum = 0
    for right in range(len(arr)):
        subArraySum += arr[right]
        while subArraySum >= d:
            subArraySum -= arr[left]
            left += 1
        currentSubArrayLength = right - left + 1
        minSubArrayLength = min(currentSubArrayLength, minSubArrayLength)
    return 0 if minSubArrayLength == float('inf') else minSubArrayLength
        
print(f"minWindowSubArraySumLessThanD: {minWindowSubArraySumLessThanD([2, 1, 5, 2, 3, 2], 7)}")

"""
Longest Substring After Replacement
    Problem: 
        Given a string S containing only uppercase English letters, 
        and an integer K, 
        find the length of the longest substring you can obtain 
        by changing at most K characters.
    input: s = "AABABBA", K = 1
    output: 4
    Explanation:
        Replace the one 'A' in the middle with 'B' and form "AABBBBA". 
        The longest substring is "BBBB" with length 4.
"""

def longestSubstringAfterReplacement(s: str, k: int):
    left = 0
    freq_map = {}
    max_repeat_count = 0
    final_window_length = 0
    for right in range(len(s)):
        if s[right] in freq_map:
            freq_map[s[right]] += 1
        else:
            freq_map[s[right]] = 1
        max_repeat_count = max(max_repeat_count, freq_map[s[right]])
        while right - left + 1 - max_repeat_count > k:
            freq_map[s[left]] -= 1
            left += 1
        final_window_length = max(final_window_length, right - left + 1)
    return final_window_length
        
print(f"longestSubstringAfterReplacement: {longestSubstringAfterReplacement("AABABBA", 1)}")
