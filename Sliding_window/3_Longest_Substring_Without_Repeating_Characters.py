# 3
# Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""
Given a string s, 
find the length of the longest 
substring without repeating characters.
"""

"""
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""


s = "pwwkew"

def getLongestSubString(s: str)-> int:
    charSet = set()
    l = 0
    res = 0
    
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res



print(getLongestSubString(s))
