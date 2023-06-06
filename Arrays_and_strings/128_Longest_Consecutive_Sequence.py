"""
Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""
nums = [3,1,6,3,6,3,2,5]

def longestConsecutive(nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            print(f'Vamos en: {n}')
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                print(f'No tenemos: {n-1}, Es inicio {n}')
                length = 1
                print(f'Tenemos al menos: {length} de largo empezando en: {n}')
                while (n + length) in numSet:
                    print(f'Si tenemos: {n + length}')
                    length += 1
                    print(f'Tenemos al menos: {length} de largo empezando en: {n}')
                longest = max(length, longest)
        return longest


result = longestConsecutive(nums)
print(f'Longest Consecutive is:{result}')


# def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums)
#         longest = 0

#         for n in nums:
#             # check if its the start of a sequence
#             if (n - 1) not in numSet:
#                 length = 1
#                 while (n + length) in numSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest

        # longest_streak = 0
        # num_set = set(nums)

        # for num in num_set:
        #     if num - 1 not in num_set:
        #         current_num = num
        #         current_streak = 1

        #         while current_num + 1 in num_set:
        #             current_num += 1
        #             current_streak += 1

        #         longest_streak = max(longest_streak, current_streak)

        # return longest_streak