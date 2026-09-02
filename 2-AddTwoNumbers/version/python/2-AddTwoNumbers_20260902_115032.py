# Last updated: 9/2/2026, 11:50:32 AM
1class Solution:
2    def combinationSum(self, candidates, target):
3        result = []
4
5        def backtrack(start, remaining, current):
6            if remaining == 0:
7                result.append(current[:])
8                return
9
10            if remaining < 0:
11                return
12
13            for i in range(start, len(candidates)):
14                current.append(candidates[i])
15
16                backtrack(
17                    i,
18                    remaining - candidates[i],
19                    current
20                )
21
22                current.pop()
23
24        backtrack(0, target, [])
25
26        return result