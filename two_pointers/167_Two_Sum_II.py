# 0167
# Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.
"""
numbers = [2,7,11,15]
target = 9
output = [1,2]


def getSum(numbers:list[int], target:int)->list[int]:
    l = 0
    r = len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            return [l + 1,r + 1]

result = getSum(numbers, target)
print(result == output)
    

