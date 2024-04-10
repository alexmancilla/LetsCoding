nums = [0]


def get_ones(nums):
    max_count = 0
    count = 0
    l_ptr = 0
    r_ptr = 0
    while r_ptr <= len(nums) - 1:
        if nums[r_ptr] != 1:
            r_ptr += 1
            l_ptr = r_ptr
            count = 0
        else:
            count += 1
            r_ptr += 1
            max_count = max(max_count, count)
    return max_count
        
        
sol = get_ones(nums)
print(sol)