# Last updated: 9/2/2026, 12:40:36 PM
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        seen = {}

        for i, num in enumerate(nums):
            if num in seen and i - seen[num] <= k:
                return True

            seen[num] = i

        return False