# Last updated: 9/2/2026, 12:28:50 PM
1class Solution:
2    def isPowerOfTwo(self, n):
3        return n > 0 and (n & (n - 1)) == 0