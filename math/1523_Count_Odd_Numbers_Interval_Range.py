# 1523. Count Odd Numbers in an Interval Range
"""
Given two non-negative integers low and high. 
Return the count of odd numbers between low and high (inclusive).
"""
"""
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
"""
low = 21
high = 22

def countOddNums(low: int, high: int)-> int:
    count = 0
    dif = (high - low) + 1 
    count = dif // 2
    if dif % 2 != 0:
        if low % 2 != 0:
            return count + 1
    return count
sol = countOddNums(low, high)
print(sol)

