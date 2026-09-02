# Last updated: 9/2/2026, 11:40:26 AM
1class Solution:
2    def reverse(self, x):
3        sign = -1 if x < 0 else 1
4        x = abs(x)
5
6        result = int(str(x)[::-1]) * sign
7
8        if result < -(2**31) or result > 2**31 - 1:
9            return 0
10
11        return result