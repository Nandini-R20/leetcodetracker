# Last updated: 9/2/2026, 11:54:24 AM
1class Solution:
2    def permute(self, nums):
3        result = []
4
5        def backtrack(current, remaining):
6            if not remaining:
7                result.append(current[:])
8                return
9
10            for i in range(len(remaining)):
11                current.append(remaining[i])
12
13                backtrack(
14                    current,
15                    remaining[:i] + remaining[i + 1:]
16                )
17
18                current.pop()
19
20        backtrack([], nums)
21
22        return result