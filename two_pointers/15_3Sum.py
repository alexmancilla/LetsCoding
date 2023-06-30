nums = [-1,0,1,2,-1,-4]



def threeSum(nums: list[int]) -> list[list[int]]:
    sol = []
    l = 0
    r = len(nums)-1

    while l < r:
        for k in range(l + 1,r):
            sum3 = nums[l] + nums[r] + nums[k]
            if (sum3 == 0):
                sol.append([nums[l],nums[r],nums[k]])
        l += 1
        r -= 1

        
    
    return sol

sol = threeSum(nums)
print(sol)
