def is_palindrome(string):
    return string == string[::-1]

def PalindromeCreator(s):
    if is_palindrome(s):
        return s

    # Check if removing one character creates a palindrome
    for i in range(len(s)):
        new_s= s[:i] + s[i+1:]
        if is_palindrome(new_s) and len(new_s) > 2:
            return s[i]

    # Check if removing two characters creates a palindrome
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            new_s = s[:i] + s[i+1:j] + s[j+1:]
            if is_palindrome(new_s) and len(new_s) > 2:
                return s[i:j+1]  # Fix: Include the character at index j

    return "not possible"


print(PalindromeCreator(input()))