# Last updated: 9/2/2026, 12:39:48 PM
class Solution:
    def countBits(self, n):
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)

        return result