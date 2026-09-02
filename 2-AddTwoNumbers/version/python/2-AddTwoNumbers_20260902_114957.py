# Last updated: 9/2/2026, 11:49:57 AM
1class Solution:
2    def isValidSudoku(self, board):
3        rows = [set() for _ in range(9)]
4        cols = [set() for _ in range(9)]
5        boxes = [set() for _ in range(9)]
6
7        for r in range(9):
8            for c in range(9):
9                value = board[r][c]
10
11                if value == '.':
12                    continue
13
14                box = (r // 3) * 3 + (c // 3)
15
16                if value in rows[r]:
17                    return False
18
19                if value in cols[c]:
20                    return False
21
22                if value in boxes[box]:
23                    return False
24
25                rows[r].add(value)
26                cols[c].add(value)
27                boxes[box].add(value)
28
29        return True