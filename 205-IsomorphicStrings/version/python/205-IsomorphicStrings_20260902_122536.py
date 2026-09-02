# Last updated: 9/2/2026, 12:25:36 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums, k):
3        seen = {}
4
5        for i, num in enumerate(nums):
6            if num in seen and i - seen[num] <= k:
7                return True
8
9            seen[num] = i
10
11        return False