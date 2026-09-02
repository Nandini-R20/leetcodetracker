# Last updated: 9/2/2026, 11:49:41 AM
1class Solution:
2    def searchInsert(self, nums, target):
3        left = 0
4        right = len(nums)
5
6        while left < right:
7            mid = (left + right) // 2
8
9            if nums[mid] < target:
10                left = mid + 1
11            else:
12                right = mid
13
14        return left