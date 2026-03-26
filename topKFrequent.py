from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        key = {}
        for item in nums:
            if item in key:
                key[item] = key[item] + 1
            else:
                key[item] = 1
        res = []
        for i in range(k):
            ele = max(key, key=key.get)
            res.append(ele)
            del key[ele]
        return res

sol = Solution()
print(sol.topKFrequent([1, 1,2, 2, 3, 3, 3], 2))

