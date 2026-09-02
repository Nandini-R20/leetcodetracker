# Last updated: 9/2/2026, 12:40:07 PM
class Solution:
    def missingNumber(self, nums):
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)