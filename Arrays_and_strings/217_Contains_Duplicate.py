nums = [1,2,3] 

def contains_duplicate(nums: list[int]) -> bool:
    st = set()
    for num in nums:
        if num not in st:
            st.add(num)
        else:
            return True
    return False
a = contains_duplicate(nums)
print(a)
