# Last updated: 9/2/2026, 12:41:41 PM
class Solution:
    def singleNumber(self, nums):
        answer = 0

        for num in nums:
            answer ^= num

        return answer