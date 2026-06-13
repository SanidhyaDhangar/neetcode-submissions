class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in s:
                curr = num
                l = 1
                while (curr + 1) in s:
                    curr += 1
                    l += 1
                res = max(res, l)
        return res