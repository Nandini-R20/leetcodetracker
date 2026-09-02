# Last updated: 9/2/2026, 12:46:16 PM
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)

        if n % 2 == 1:
            return nums[n // 2]

        return (nums[n // 2 - 1] + nums[n // 2]) / 2