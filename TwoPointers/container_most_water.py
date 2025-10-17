"""
You are given an integer array height of length N. 
There are N vertical lines drawn such that the two endpoints of the ith line are (i,0) 
and (i,height[i]). 
Find two lines that together with the x-axis form a container, 
such that the container holds the most water. 
Return the maximum amount of water the container can store.
"""

def maxArea(heights: list[int]):
    max_area = 0
    left, right = 0, len(heights) - 1
    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        area = height * width
        max_area = max(max_area, area)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area

print(f"maxArea: {maxArea([1,7,2,5,4,7,3,6])}")