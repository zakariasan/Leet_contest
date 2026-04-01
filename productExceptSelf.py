from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for ind, item in enumerate(nums):
            left = nums[:ind]
            right = nums[ind + 1:]
            nbr = 1
            nbr = list(map(lambda x: nbr = nbr * x, left + right))
            res.append(nbr)
        print(res)
        return res 


sol = Solution()


sol.productExceptSelf([1, 2, 4, 6, 33, 1337, 0])
