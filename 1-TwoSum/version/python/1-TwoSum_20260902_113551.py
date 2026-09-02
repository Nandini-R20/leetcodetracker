# Last updated: 9/2/2026, 11:35:51 AM
1class Solution:
2    def twoSum(self, nums, target):
3        seen = {}
4        for i, num in enumerate(nums):
5            need = target - num
6            if need in seen:
7                return [seen[need], i]
8            seen[num] = i