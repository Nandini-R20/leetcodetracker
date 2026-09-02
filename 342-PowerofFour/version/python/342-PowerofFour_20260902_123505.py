# Last updated: 9/2/2026, 12:35:05 PM
1class Solution:
2    def isPowerOfFour(self, n):
3        if n <= 0:
4            return False
5
6        while n % 4 == 0:
7            n //= 4
8
9        return n == 1