# 88
# Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
"""
You are given two integer arrays nums1 and nums2, 
sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
"""

""""
Input: 

nums1 = [1,2,3,0,0,0], m = 3
        l = m + n  ^ 
nums1 = [1,2,3,0,0,0], m = 3
           m ^ 

nums2 = [2,5,6], n = 3
           n ^                 



Output: [1,2,2,3,5,6]
"""


# Aproach 
# Instead of going in the normal direction and look for a way to append the numbers in the proper order we wil be doing backwards
# Going backwards to take advantage of the space that we already have
# Use pointers 
# Compare m and n and append to the nums1[l] the bigger
# Taking advante that both list are already sorted

nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3
Output = [1,2,2,3,5,6]

def mergeSorted(nums1: list[int], m: int, nums2: list[int], n):
    # Pointers
    last = (m + n) - 1
    # m 
    # n
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1 
    
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1


    return nums1


sol = mergeSorted(nums1, m, nums2,n)
print(Output == sol)


