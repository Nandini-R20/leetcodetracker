# Last updated: 9/2/2026, 12:40:23 PM
class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0