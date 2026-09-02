# Last updated: 9/2/2026, 12:34:44 PM
1class Solution:
2    def countBits(self, n):
3        result = [0] * (n + 1)
4
5        for i in range(1, n + 1):
6            result[i] = result[i >> 1] + (i & 1)
7
8        return result