# Last updated: 9/2/2026, 12:43:28 PM
class Solution:
    def combine(self, n, k):
        result = []

        def backtrack(start, current):
            if len(current) == k:
                result.append(current[:])
                return

            for i in range(start, n + 1):
                current.append(i)
                backtrack(i + 1, current)
                current.pop()

        backtrack(1, [])

        return result