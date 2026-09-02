# Last updated: 9/2/2026, 12:34:00 PM
1class Solution:
2    def isPowerOfThree(self, n):
3        if n <= 0:
4            return False
5
6        while n % 3 == 0:
7            n //= 3
8
9        return n == 1