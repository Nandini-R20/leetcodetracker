# Last updated: 9/2/2026, 12:42:59 PM
class Solution:
    def grayCode(self, n):
        result = [0]

        for i in range(n):
            add = 1 << i

            for j in range(len(result) - 1, -1, -1):
                result.append(result[j] + add)

        return result