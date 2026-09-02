# Last updated: 9/2/2026, 11:55:47 AM
1class Solution:
2    def solveNQueens(self, n):
3        result = []
4        board = [["."] * n for _ in range(n)]
5        cols = set()
6        diag1 = set()
7        diag2 = set()
8
9        def backtrack(row):
10            if row == n:
11                result.append(["".join(r) for r in board])
12                return
13
14            for col in range(n):
15                if col in cols or row - col in diag1 or row + col in diag2:
16                    continue
17
18                board[row][col] = "Q"
19                cols.add(col)
20                diag1.add(row - col)
21                diag2.add(row + col)
22
23                backtrack(row + 1)
24
25                board[row][col] = "."
26                cols.remove(col)
27                diag1.remove(row - col)
28                diag2.remove(row + col)
29
30        backtrack(0)
31        return result