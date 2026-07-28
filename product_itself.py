
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i, item in enumerate(nums):
            va = 1
            for j, value2 in enumerate(nums):
                if i != j:
                    va *= value2
            res.append(va)
        print(res)




sol = Solution()


sol.productExceptSelf([-1,0,1,2,3])
