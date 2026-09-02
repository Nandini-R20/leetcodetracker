# Last updated: 9/2/2026, 12:33:39 PM
1class NumArray:
2
3    def __init__(self, nums):
4        self.nums = nums
5
6    def sumRange(self, left, right):
7        return sum(self.nums[left:right + 1])