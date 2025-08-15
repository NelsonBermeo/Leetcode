nums = [2,3,4,5,6,8]
def contains_dup(arr):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
