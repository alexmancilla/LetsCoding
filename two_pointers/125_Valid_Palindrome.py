"""
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
s = "A man, a plan, a canal: Panama"

# ascii values for lower case from 97 to 122
def validPalindrome(s: str) -> bool:
    new_string = ''
    lowerString = s.lower()

    # creating clean string
    for char in lowerString:
        if ord(char) >= 97 and ord(char) <= 122:
            new_string += char
        
    # pointers
    l = 0
    r = len(new_string) - 1

    # evaluating validity
    while l < r:
        if new_string[l] != new_string[r]:
            return False
        l += 1
        r -= 1

    return True

sol = validPalindrome(s)
print(sol)