# Last updated: 9/2/2026, 11:52:15 AM
1class Solution:
2    def combinationSum2(self, candidates, target):
3        candidates.sort()
4        result = []
5
6        def backtrack(start, remaining, current):
7            if remaining == 0:
8                result.append(current[:])
9                return
10
11            if remaining < 0:
12                return
13
14            for i in range(start, len(candidates)):
15                if i > start and candidates[i] == candidates[i - 1]:
16                    continue
17
18                if candidates[i] > remaining:
19                    break
20
21                current.append(candidates[i])
22
23                backtrack(
24                    i + 1,
25                    remaining - candidates[i],
26                    current
27                )
28
29                current.pop()
30
31        backtrack(0, target, [])
32
33        return result