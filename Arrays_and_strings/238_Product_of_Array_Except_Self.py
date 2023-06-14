"""
Given an integer array nums, 
return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""

nums = [-1,1,0,-3,3]

def productOfArray(nums: list[int])->list[int]:
    answer = [1] * (len(nums))
    product = 1

    for num in nums:
        product *= num

    for ans in range(len(nums)):
        answer.append(product // nums[ans])
    return answer




sol = productOfArray(nums)
print(sol)
