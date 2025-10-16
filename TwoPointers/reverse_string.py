"""
Write a function that reverses a string. 
The input is given as an array of characters s. 
You must do this by modifying the input array in-place with O(1) extra memory.
"""

def getReverseString(s: str) -> str:
    left, right = 0, len(s) - 1
    s = list(s)
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)

print(f"Reverse: {getReverseString("Was it a car or a cat I saw?")}")