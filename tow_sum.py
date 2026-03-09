class Solution:
    def get_index(self, nums, less):
        out = []
        print("-0------------------------")
        for value in less:
            tmp = nums.index(value)
            if tmp in out:
                tmp = tmp + 1 + nums[tmp + 1:].index(value)
            out.append(tmp)
        return out

    def towSum(self, nums, target):
        less = list(filter(lambda x: x<= target, nums))
        last = []
        if (sum(less) == target):
            return self.get_index(nums, less)
        else:
            tmp = sum(less) - target
            if tmp in less:
                less.remove(tmp)
                return self.get_index(nums, less)
            return None


sol = Solution()

vv = sol.towSum([-3,4,3,90], 0)

print(vv, type(vv))


