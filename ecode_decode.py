from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for ind, item in enumerate(strs):
            for ch in item:
                res.append(chr(ord(ch) ^ 7))
            if (ind < len(strs)):
                res.append(".")
        return ''.join(res)

    def decode(self, s: str) -> List[str]:
        res = s.split(".")
        result = []
        for item in res:
            out = []
            for ch in item:
                out.append(chr(ord(ch) ^ 7))
            result.append(''.join(out))
            del out

        return result


sol = Solution()

end = sol.encode([])
print(end)
print(sol.decode(end))
