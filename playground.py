"""
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.
"""

"""
You must write an algorithm that runs in O(n) time.
"""

# Input: nums = [100,4,200,1,3,2]

# Output: 4

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
#  a set will save the numbers and whe can acces O(1) to check if exists
# Iterate over the list and check if is start or is part of a sequence
# if not we need to look for the start of that sequence and pass that number
# If its start we can star count :
#   we need cout for element + 1, 
#       we need to store that individual count and check if its the max count


nums = [9,1,4,7,3,-1,0,5,8,-1,6]

def getLongest(nums: list[int])-> int:
    numset = set(nums)
    longest = 0
    

    for number in nums:
        start = number - 1
        if start not in numset:
            streak = 1
            while(number + streak) in numset:
                    streak += 1
                    
            longest = max(streak, longest)
            
    return longest


        


sol = getLongest(nums)
print(sol)