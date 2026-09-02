# Last updated: 9/2/2026, 12:46:11 PM
class Solution:
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)

        result = int(str(x)[::-1]) * sign

        if result < -(2**31) or result > 2**31 - 1:
            return 0

        return result