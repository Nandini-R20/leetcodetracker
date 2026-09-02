# Last updated: 9/2/2026, 11:40:07 AM
1class Solution:
2    def convert(self, s, numRows):
3        if numRows == 1 or numRows >= len(s):
4            return s
5
6        rows = [""] * numRows
7        row = 0
8        direction = 1
9
10        for ch in s:
11            rows[row] += ch
12
13            if row == 0:
14                direction = 1
15            elif row == numRows - 1:
16                direction = -1
17
18            row += direction
19
20        return "".join(rows)