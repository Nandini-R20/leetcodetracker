# Last updated: 9/2/2026, 12:24:23 PM
1class Solution:
2    def countPrimes(self, n):
3        if n <= 2:
4            return 0
5
6        prime = [True] * n
7        prime[0] = prime[1] = False
8
9        for i in range(2, int(n ** 0.5) + 1):
10            if prime[i]:
11                for j in range(i * i, n, i):
12                    prime[j] = False
13
14        return sum(prime)