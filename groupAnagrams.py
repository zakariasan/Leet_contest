from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for item in strs:
            if len(res) == 0:
                res[item] = [item]
            else:
                # logic here
                len_res = len(res)
                for ele in res.keys():
                    for n_ele in item:
                        if n_ele not in ele:
                            res[item] = item
                            break
                if len_res == len(res):
                    res[item] = [item]
        return res


solution = Solution()
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(strs)
print()
print(solution.groupAnagrams(strs))
