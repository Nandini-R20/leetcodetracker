# Last updated: 9/2/2026, 12:45:46 PM
class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return

            for ch in letters[digits[index]]:
                backtrack(index + 1, current + ch)

        backtrack(0, "")

        return result