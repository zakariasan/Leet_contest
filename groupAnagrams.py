from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if (len(strs) <= 1):
            return [strs]
        else:
            res = {}
            for item in strs:
                to_search = ''.join(sorted(item))
                if to_search in res:
                    res[to_search] = res[to_search] + [item]
                else:
                    res[to_search] = [item]
            return list(res.values())

solution = Solution()
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(strs)
print()
print(solution.groupAnagrams(strs))
