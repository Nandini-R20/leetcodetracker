# Last updated: 9/2/2026, 12:44:35 PM
class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        result = 1

        while n:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        return result