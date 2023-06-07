"""
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""
s = ["h","e","l","l","o"]

def reverseString(s: list[str]):
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1
        while l < r:
                temp = s[l]
                s[l] = s[r]
                s[r] = temp 
                l += 1
                r -= 1
        print(s)


reverseString(s)