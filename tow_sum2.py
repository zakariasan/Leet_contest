def tow_sum(nums, target):
    for ind, value in enumerate(nums):
        need = target - value
        if need in nums[ind + 1:]:
            return [ind, nums[ind + 1:].index(need)]
    return None


tow_sum([2, 7, 11, 15], 9)
