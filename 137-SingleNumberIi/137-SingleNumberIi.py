# Last updated: 9/2/2026, 12:41:40 PM
class Solution:
    def singleNumber(self, nums):
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones