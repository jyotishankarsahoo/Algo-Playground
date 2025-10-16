"""
Given two strings s and t, 
return true if the two strings are anagrams of each other, 
otherwise return false.
"""

def isAnagramSort(s: str, t: str):
    return sorted(s) == sorted(t)

def isAnagramHashmap(s: str, t: str):
    if len(s) != len(t):
        return False

    s_count = {}

    for char in s:
        if char in s_count:
            s_count[char] += 1
        else:
            s_count[char] = 1

    for char in t:
        if char not in s_count:
            return False
        s_count[char] -= 1
        if s_count[char] == 0:
            del s_count[char]
    return len(s_count) == 0
    

print(f"Is Anagram: {isAnagramSort("racecar", "carrace")}")
print(f"Is Anagram: {isAnagramSort("jar", "jam")}")
print(f"Is Anagram: {isAnagramSort("aabcc", "aaabc")}")
print("*" * 20)
print(f"Is Anagram: {isAnagramHashmap("racecar", "carrace")}")
print(f"Is Anagram: {isAnagramHashmap("jar", "jam")}")
print(f"Is Anagram: {isAnagramHashmap("aabcc", "aaabc")}")
