"""
Given an integer array nums, 
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""

nums = [-1,1,0,-3,3]

def productOfArray(nums: list[int])->list[int]:
    n = len(nums)
    res = [1] * (n)
    prefix = 1

    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    postFix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postFix
        postFix *= nums[i]
    return res

sol = productOfArray(nums)
print(sol)
