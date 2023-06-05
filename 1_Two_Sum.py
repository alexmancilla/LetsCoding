# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2,11,15]

def getTwoSum(nums: list[int], target: int) -> list[int]:
    # n = len(nums)
    # for i in range(n - 1 ):
    #     for j  in range(i + 1, n):
            # if nums[i] + nums[j] == target:
            #     print(nums[i], nums[j])
    l = 0
    r = len(nums) - 1
    while l <= r:
        if nums[l] + nums[r] == target:
            print(nums[l], nums[r])
        elif nums[l] + nums[r] > target:
            r -= 1
        else: 
            l += 1
    print([])
        

getTwoSum(nums, 9)


