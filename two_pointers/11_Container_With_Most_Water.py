# 11
# Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/


height = [1,8,6,2,5,4,8,3,7]

def area(l, r, d):
    if l < r:
        return l * d
    else:
        return r * d

def maxArea(height: list[int]) -> int:
    maxWater = 0
    l = 0
    r = len(height) - 1

    while l < r:
        dif = r - l
        water = area(height[l],height[r],dif)
        maxWater = max(maxWater, water)
        
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return maxWater


sol = maxArea(height)
print(sol)