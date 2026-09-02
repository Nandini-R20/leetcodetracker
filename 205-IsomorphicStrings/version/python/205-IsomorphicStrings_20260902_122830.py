# Last updated: 9/2/2026, 12:28:30 PM
1class Solution:
2    def summaryRanges(self, nums):
3        result = []
4        i = 0
5
6        while i < len(nums):
7            start = nums[i]
8
9            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
10                i += 1
11
12            if start == nums[i]:
13                result.append(str(start))
14            else:
15                result.append(str(start) + "->" + str(nums[i]))
16
17            i += 1
18
19        return result