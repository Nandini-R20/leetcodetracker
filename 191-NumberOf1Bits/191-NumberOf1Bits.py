# Last updated: 9/2/2026, 12:40:54 PM
class Solution:
    def hammingWeight(self, n):
        count = 0
        
        while n:
            count += n & 1
            n >>= 1
        
        return count