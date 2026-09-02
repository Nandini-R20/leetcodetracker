# Last updated: 9/2/2026, 12:39:59 PM
class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left:right + 1])