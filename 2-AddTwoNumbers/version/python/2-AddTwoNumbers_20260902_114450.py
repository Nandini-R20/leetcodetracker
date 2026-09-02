# Last updated: 9/2/2026, 11:44:50 AM
1class Solution:
2    def generateParenthesis(self, n):
3        result = []
4
5        def backtrack(current, open_count, close_count):
6            if len(current) == 2 * n:
7                result.append(current)
8                return
9
10            if open_count < n:
11                backtrack(
12                    current + "(",
13                    open_count + 1,
14                    close_count
15                )
16
17            if close_count < open_count:
18                backtrack(
19                    current + ")",
20                    open_count,
21                    close_count + 1
22                )
23
24        backtrack("", 0, 0)
25
26        return result