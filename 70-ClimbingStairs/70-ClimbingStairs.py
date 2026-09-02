# Last updated: 9/2/2026, 12:43:46 PM
class Solution:
    def climbStairs(self, n):
        a = 1
        b = 1

        for _ in range(n):
            a, b = b, a + b

        return a