# Last updated: 9/2/2026, 11:49:20 AM
1class Solution:
2    def search(self, nums, target):
3        left = 0
4        right = len(nums) - 1
5
6        while left <= right:
7            mid = (left + right) // 2
8
9            if nums[mid] == target:
10                return mid
11
12            if nums[left] <= nums[mid]:
13                if nums[left] <= target < nums[mid]:
14                    right = mid - 1
15                else:
16                    left = mid + 1
17            else:
18                if nums[mid] < target <= nums[right]:
19                    left = mid + 1
20                else:
21                    right = mid - 1
22
23        return -1