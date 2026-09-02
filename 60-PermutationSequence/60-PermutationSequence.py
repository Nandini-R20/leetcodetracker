# Last updated: 9/2/2026, 12:44:09 PM
import math

class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        answer = ""

        k -= 1

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact

            answer += str(numbers.pop(index))
            k %= fact

        return answer