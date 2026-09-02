# Last updated: 9/2/2026, 12:39:54 PM
class Solution:
    def isPowerOfFour(self, n):
        if n <= 0:
            return False

        while n % 4 == 0:
            n //= 4

        return n == 1