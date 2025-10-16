"""
Given a string s, return true if it is a palindrome, otherwise return false.
"""

def isPalindromeReverseString(s: str):
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]

def isPalindromeTwoPointer(s: str):
    left, right = 0, len(s) - 1
    s = s.lower()
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(f"is Palindrome: {isPalindromeReverseString("Was it a car or a cat I saw?")}")
print(f"is Palindrome: {isPalindromeTwoPointer("Was it a car or a cat I saw?")}")