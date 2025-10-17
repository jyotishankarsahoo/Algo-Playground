
"""
    Finds the maximum sum of a contiguous sub-array and the sub-array itself 
    using

    Args:
        nums: A list of integers.

    Returns:
        A tuple containing the maximum sum (int) and the corresponding sub-array (list[int]).
"""

# A brute-force approach.
def maxSumSubArrayBrute(nums: list[int]):
    max_sum = nums[0]
    start_index = 0
    end_index = 0
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start_index = i
                end_index = j
    sub_array = nums[start_index:end_index + 1]
    return max_sum, sub_array

def maxSumSubArrayKadane(nums: list[int]):
    current_sum = 0
    max_sum = nums[0]
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)
    return max_sum

def maxSumSubArrayWithArrayKadane(nums: list[int]):
    current_sum = 0
    max_sum = nums[0]
    max_start_index = 0
    max_end_index = 0
    current_start_index = 0
    for index, num in enumerate(nums):
        if num > current_sum + num:
            current_sum = num
            current_start_index = index
        else:
            current_sum = current_sum + num
        if current_sum > max_sum:
            max_sum = current_sum
            max_start_index = current_start_index
            max_end_index = index
        sub_array = nums[max_start_index:max_end_index + 1]
    return max_sum, sub_array

print(f"Max Sum: {maxSumSubArrayBrute([4,-1,2,-7,3,4])}")
print(f"Max Sum: {maxSumSubArrayBrute([-2, 1, -3, 4, -1, 2, 1, -5, 4])}")
print(f"Max Sum: {maxSumSubArrayBrute([4,-1,2])}")

print(f"Max Sum: {maxSumSubArrayKadane([4,-1,2,-7,3,4])}")
print(f"Max Sum: {maxSumSubArrayKadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])}")
print(f"Max Sum: {maxSumSubArrayKadane([4,-1,2])}")

print(f"Max Sum: {maxSumSubArrayWithArrayKadane([4,-1,2,-7,3,4])}")
print(f"Max Sum: {maxSumSubArrayWithArrayKadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])}")
print(f"Max Sum: {maxSumSubArrayWithArrayKadane([4,-1,2])}")


