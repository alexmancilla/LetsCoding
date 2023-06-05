# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [2,2,7,11,15]

def getTwoSum(nums: list[int], target: int) -> list[int]:
    # n = len(nums)
    # for i in range(n - 1):
    #     for j in range(i + 1, n):
    #         if nums[i] + nums[j] == target:
    #             return [nums[i],nums[j]]
    # return []


    # l, r = 0, len(nums) - 1
    # while l <= r:
    #     if nums[l] + nums[r] == target:
    #         return [nums[l], nums[r]]
    #     elif nums[l] + nums[r] > target:
    #         r -= 1
    #     else:
    #         l += 1

    # return []

    hashmap = {}
    n = len(nums)
    
    for element in range(n):
        diff = target - nums[element]
        if diff in hashmap:
            return [hashmap[element], element]
        else:
            hashmap[nums[element]] = element
            

result = getTwoSum(nums, 9)
print(result)


