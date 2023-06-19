# problem = https://leetcode.com/problems/valid-parentheses/

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

# Input: s = "()[]{}"
# Output: true

s = "({)"

def isValid(s: str)->bool:
    openP = "([{"
    closeP = ")]}"
    stack = []
    valid = {')':'(',']':'[','}':'{'}

    for i in s:
        if i in openP:
            stack.append(i)
        elif i in closeP:
            if not stack:
                return False
            elif valid[i] != stack.pop():
                return False 
    if len(stack) == 0:
        return True


sol = isValid(s)
print(sol)