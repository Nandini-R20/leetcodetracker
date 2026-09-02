# Last updated: 9/2/2026, 11:41:38 AM
1class Solution:
2    def isMatch(self, s, p):
3        memo = {}
4
5        def dp(i, j):
6            if (i, j) in memo:
7                return memo[(i, j)]
8
9            if j == len(p):
10                return i == len(s)
11
12            first_match = (
13                i < len(s) and
14                (p[j] == s[i] or p[j] == '.')
15            )
16
17            if j + 1 < len(p) and p[j + 1] == '*':
18                result = (
19                    dp(i, j + 2) or
20                    (first_match and dp(i + 1, j))
21                )
22            else:
23                result = first_match and dp(i + 1, j + 1)
24
25            memo[(i, j)] = result
26            return result
27
28        return dp(0, 0)