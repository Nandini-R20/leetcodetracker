# Last updated: 9/2/2026, 12:43:22 PM
class Solution:
    def removeDuplicates(self, nums):
        k = 0

        for num in nums:
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1

        return k