# Last updated: 9/2/2026, 11:54:48 AM
1class Solution:
2    def rotate(self, matrix):
3        n = len(matrix)
4
5        for i in range(n):
6            for j in range(i + 1, n):
7                matrix[i][j], matrix[j][i] = (
8                    matrix[j][i],
9                    matrix[i][j]
10                )
11
12        for row in matrix:
13            row.reverse()