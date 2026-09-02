# Last updated: 9/2/2026, 11:54:36 AM
1class Solution:
2    def permuteUnique(self, nums):
3        nums.sort()
4        result = []
5        used = [False] * len(nums)
6
7        def backtrack(current):
8            if len(current) == len(nums):
9                result.append(current[:])
10                return
11
12            for i in range(len(nums)):
13                if used[i]:
14                    continue
15
16                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
17                    continue
18
19                used[i] = True
20                current.append(nums[i])
21
22                backtrack(current)
23
24                current.pop()
25                used[i] = False
26
27        backtrack([])
28
29        return result