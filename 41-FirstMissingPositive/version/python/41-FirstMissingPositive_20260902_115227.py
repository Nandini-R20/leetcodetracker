# Last updated: 9/2/2026, 11:52:27 AM
1class Solution:
2    def firstMissingPositive(self, nums):
3        n = len(nums)
4
5        for i in range(n):
6            while (
7                1 <= nums[i] <= n
8                and nums[nums[i] - 1] != nums[i]
9            ):
10                correct = nums[i] - 1
11                nums[i], nums[correct] = nums[correct], nums[i]
12
13        for i in range(n):
14            if nums[i] != i + 1:
15                return i + 1
16
17        return n + 1