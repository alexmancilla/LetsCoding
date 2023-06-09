"""
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""
# s = "A man, a plan, a canal: Panama"
s = '0P'

# ascii values for lower case from 97 to 122
def validPalindrome(s: str) -> bool:
    new_string = ''
    lowerString = s.lower()


    def isAlpha(c):
        if ord(char) >= ord("a") and ord(char) <= ord("z"):
            return True
        elif ord(char) >= ord("0") and ord(char) <= ord("9"):
            return True
        else:
            return False

    # creating clean string
    for char in lowerString:
        if isAlpha(char):
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


