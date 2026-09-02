# Last updated: 9/2/2026, 12:39:50 PM
class Solution:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1