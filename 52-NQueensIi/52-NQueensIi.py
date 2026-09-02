# Last updated: 9/2/2026, 12:44:29 PM
class Solution:
    def totalNQueens(self, n):
        answer = 0
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row):
            nonlocal answer

            if row == n:
                answer += 1
                return

            for col in range(n):
                if col in cols or row - col in diag1 or row + col in diag2:
                    continue

                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return answer