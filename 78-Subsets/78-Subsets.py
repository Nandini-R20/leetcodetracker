# Last updated: 9/2/2026, 12:43:25 PM
class Solution:
    def subsets(self, nums):
        result = []

        def backtrack(index, current):
            result.append(current[:])

            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])

        return result