# Last updated: 9/2/2026, 12:44:40 PM
class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = (
                    matrix[j][i],
                    matrix[i][j]
                )

        for row in matrix:
            row.reverse()