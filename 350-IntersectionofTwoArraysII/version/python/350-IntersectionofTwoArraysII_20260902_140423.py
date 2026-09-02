# Last updated: 9/2/2026, 2:04:23 PM
1class Solution:
2    def intersect(self, nums1, nums2):
3        result = []
4
5        for num in nums1:
6            if num in nums2:
7                result.append(num)
8                nums2.remove(num)
9
10        return result