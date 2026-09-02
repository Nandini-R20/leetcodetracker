# Last updated: 9/2/2026, 12:40:43 PM
class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0] = prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                for j in range(i * i, n, i):
                    prime[j] = False

        return sum(prime)