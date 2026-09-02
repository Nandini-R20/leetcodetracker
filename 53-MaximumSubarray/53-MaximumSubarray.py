# Last updated: 9/2/2026, 12:44:26 PM
class Solution:
    def maxSubArray(self, nums):
        current = nums[0]
        answer = nums[0]

        for num in nums[1:]:
            current = max(num, current + num)
            answer = max(answer, current)

        return answer