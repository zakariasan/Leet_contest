class Solution:
    def costum(self, order, s) -> str:
        out = []
        for item in order:
            if item in s:
                out.append(''.join(list(filter(lambda x: x == item, s))))
        for item in s:
            if item not in out:
                out.append(item)
        print(out)


sol = Solution()
sol.costum("kqep", "pekeq")
