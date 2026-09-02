# Last updated: 9/2/2026, 11:50:22 AM
1class Solution:
2    def countAndSay(self, n):
3        result = "1"
4
5        for _ in range(n - 1):
6            current = ""
7            i = 0
8
9            while i < len(result):
10                j = i
11
12                while j < len(result) and result[j] == result[i]:
13                    j += 1
14
15                current += str(j - i) + result[i]
16                i = j
17
18            result = current
19
20        return result