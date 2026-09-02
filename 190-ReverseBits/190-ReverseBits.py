# Last updated: 9/2/2026, 12:40:57 PM
class Solution:
    def reverseBits(self, n):
        result = 0
        
        for i in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        
        return result