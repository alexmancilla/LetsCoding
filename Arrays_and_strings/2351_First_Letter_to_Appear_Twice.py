# Given a string s consisting of lowercase English letters, return the first letter to appear twice
# Example:
# Input: s = “abccbaacz”
# Output: “c”

s = "abccbaacz"

def first_letter_twice(s: str)-> str:
    hs = set()
    for letter in s:
        if letter in hs:
            return letter
        else:
            hs.add(letter)

print(first_letter_twice(s))
